"""This pl/sql code extract blobs from BLOBFILES table and save  them in DIRECTORY """
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