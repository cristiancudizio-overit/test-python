g_plsql_write_file_on_dir = """DECLARE
    l_dirname   VARCHAR2(30);
    l_file      UTL_FILE.FILE_TYPE;
    l_buffer    RAW(32767);
    l_amount    BINARY_INTEGER := 32767;
    l_pos       INTEGER := 1;
    l_blob_len  INTEGER;
    cursor cur_odpdumps(cp_dump_name varchar2) is
        SELECT id, dump_name, dump_file, datetime, log_file_name, log_file, notes
        from blobfiles 
        where dump_name = cp_dump_name;
    rec_odpdumps cur_odpdumps%ROWTYPE;
    BEGIN
    l_dirname := 'DATA_PUMP_DIR';
    for rec_odpdumps in cur_odpdumps(:p_file_name) loop
            l_blob_len := DBMS_LOB.getlength(rec_odpdumps.dump_file);
            l_pos := 1;
            l_amount := 32767; -- !!!
            -- Open the destination file.
            l_file := UTL_FILE.fopen(l_dirname, rec_odpdumps.dump_name, 'ab', 32767);
            -- Read chunks of the BLOB and write them to the file
            -- until complete.
            WHILE l_pos < l_blob_len LOOP
                DBMS_LOB.read(rec_odpdumps.dump_File, l_amount, l_pos, l_buffer);
                UTL_FILE.put_raw(l_file, l_buffer, TRUE);
                l_pos := l_pos + l_amount;
            END LOOP;
            -- Close the file.
            UTL_FILE.fclose(l_file);
            --log 
            l_blob_len := DBMS_LOB.getlength(rec_odpdumps.log_file);
            l_pos := 1;
            l_amount := 32767; -- !!!
            -- Open the destination file.
            if (rec_odpdumps.log_file_name is not null) then
                l_file := UTL_FILE.fopen(l_dirname, rec_odpdumps.log_file_name, 'ab', 32767);
                -- Read chunks of the BLOB and write them to the file
                -- until complete.
                WHILE l_pos < l_blob_len LOOP
                    DBMS_LOB.read(rec_odpdumps.log_file, l_amount, l_pos, l_buffer);
                    UTL_FILE.put_raw(l_file, l_buffer, TRUE);
                    l_pos := l_pos + l_amount;
                END LOOP;
                -- Close the file.
                UTL_FILE.fclose(l_file);
            end if;
    end loop;
    EXCEPTION
    WHEN OTHERS THEN
        -- Close the file if something goes wrong.
        IF UTL_FILE.is_open(l_file) THEN
        UTL_FILE.fclose(l_file);
        END IF;
        RAISE;
    END;"""
g_plsql_write_mreti_on_dir = """DECLARE
    l_dirname   VARCHAR2(30);
    l_file      UTL_FILE.FILE_TYPE;
    l_buffer    RAW(32767);
    l_amount    BINARY_INTEGER := 32767;
    l_pos       INTEGER := 1;
    l_blob_len  INTEGER;
    cursor cur_odpdumps(cp_dump_name varchar2) is
        SELECT id, dump_name, dump_file, datetime, log_file_name, log_file, notes,
        -- to do: python need '\\' for escape
        case   substr(upper(substr(dump_name,1+instr(dump_name,'\\', -1))),1,4)
           when 'MARE' THEN 'MAREEISTAT.csv'
           when 'MRET' THEN 'MRETI.csv'
        end dest_file_name
        from blobfiles 
        where dump_name = cp_dump_name;
    rec_odpdumps cur_odpdumps%ROWTYPE;
    BEGIN
    l_dirname := 'DATA_PUMP_DIR';
    for rec_odpdumps in cur_odpdumps(:p_file_name) loop
            l_blob_len := DBMS_LOB.getlength(rec_odpdumps.dump_file);
            l_pos := 1;
            l_amount := 32767; -- !!!
            -- Open the destination file.
            l_file := UTL_FILE.fopen(l_dirname, rec_odpdumps.dest_file_name, 'ab', 32767);
            -- Read chunks of the BLOB and write them to the file
            -- until complete.
            WHILE l_pos < l_blob_len LOOP
                DBMS_LOB.read(rec_odpdumps.dump_File, l_amount, l_pos, l_buffer);
                UTL_FILE.put_raw(l_file, l_buffer, TRUE);
                l_pos := l_pos + l_amount;
            END LOOP;
            -- Close the file.
            UTL_FILE.fclose(l_file);
    end loop;
    EXCEPTION
    WHEN OTHERS THEN
        -- Close the file if something goes wrong.
        IF UTL_FILE.is_open(l_file) THEN
        UTL_FILE.fclose(l_file);
        END IF;
        RAISE;
    END;"""
g_plsql_load_blob_from_dir = """DECLARE
        l_bfile BFILE;
        l_blob BLOB;
        l_bfilelog BFILE;
        l_bloblog BLOB;
        l_directory varchar2(30);
        l_dumpfilename varchar2(60);
        l_logfilename varchar2(60);
        l_dest_offset integer;
        l_src_offset integer;
        BEGIN
        l_directory := 'DATA_PUMP_DIR';
        l_dumpfilename := :p_dumpfilename';
        l_logfilename :=  _p_logfilename;
        l_bfile := BFILENAME(l_directory, l_dumpfilename);
        l_bfilelog := BFILENAME(l_directory, l_logfilename);
        insert into blobfiles (
        id, 
        dump_name,
        dump_file, 
        datetime, 
        log_file_name, 
        log_file, 
        notes)
        values (
        blobfiles_seq.nextval,
        l_dumpfilename,
        empty_blob(),
        sysdate,
        l_logfilename,
        empty_blob(),
        'test') 
        returning dump_file, log_file into l_blob, l_bloblog;
        l_dest_offset := 1;
        l_src_offset := 1;
        dbms_lob.fileopen(l_bfile, dbms_lob.FILE_READONLY);
        dbms_lob.LOADBLOBFROMFILE ( l_blob, l_bfile, dbms_lob.getlength(l_bfile), l_dest_offset, l_src_offset);
        dbms_lob.fileclose( l_bfile );
        l_dest_offset := 1;
        l_src_offset := 1;
        if (l_logfilename is not null) then
            dbms_lob.fileopen(l_bfilelog, dbms_lob.FILE_READONLY);
            dbms_lob.LOADBLOBFROMFILE ( l_bloblog, l_bfilelog, dbms_lob.getlength(l_bfilelog), l_dest_offset, l_src_offset);
            dbms_lob.fileclose( l_bfilelog );
        end if;
        COMMIT;
        END;"""
