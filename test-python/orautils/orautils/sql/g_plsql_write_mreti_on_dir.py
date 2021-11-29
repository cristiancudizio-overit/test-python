""""this code save blob from BLOBFILES table to DIRECTORY concatenating they into MRETI.csv or MAREEISTAT.csv"""
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
           else substr(dump_name,1+instr(dump_name,'\\', -1))
        end dest_file_name
        from blobfiles 
        where UPPER(dump_name) LIKE  '%'||cp_dump_name||'%';
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