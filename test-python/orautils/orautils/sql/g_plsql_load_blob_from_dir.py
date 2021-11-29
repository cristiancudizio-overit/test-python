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
        l_directory := :p_directory;
        l_dumpfilename := :p_dumpfilename;
        l_logfilename :=  :p_logfilename;
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