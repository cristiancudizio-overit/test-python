g_plsql_dpimp = """DECLARE
        p_src_username varchar2(30) := '{.p_src_username}'; 
        p_des_username varchar2(30) := '{.p_des_username}';
        p_dumpfilename varchar2(60) := '{.p_dumpfilename}';
        p_directory varchar2(30) := '{.p_directory}';
        p_src_tbs1 varchar2(30) := '{.p_src_tbs1}';
        p_des_tbs1 varchar2(30) := '{.p_des_tbs1}';
        p_src_tbs2 varchar2(30) := '{.p_src_tbs2}';
        p_des_tbs2 varchar2(30) := '{.p_des_tbs2}';
        p_src_tbs3 varchar2(30) := '{.p_src_tbs3}';
        p_des_tbs3 varchar2(30) := '{.p_des_tbs3}';
    -- ver 1.2
    -- date: 13/05/2021
    -- notes: changed wait_for_job
    -- ver 1.1 
    -- date: 02/10/2020
    -- ver 1.0 
    -- date: 27/04/2018
    v_handle number;
    v_logfilename varchar2(40);
    v_dumpfilename varchar2(40);
    v_src_username varchar2(30);
    v_des_username varchar2(30);
    l_state varchar2(30) := 'NONE';
    l_status ku$_status;
    begin
    v_src_username := upper(p_src_username);
    v_des_username := upper(p_des_username);
    if (p_dumpfilename='x') then
        v_dumpfilename := v_src_username||'.dpdmp';
    else
        v_dumpfilename := p_dumpfilename;
    end if;
    v_logfilename  := 'imp_'||v_des_username||'.log';
    v_handle := dbms_datapump.open( operation => 'IMPORT', 
                                    job_mode =>'SCHEMA', 
                                    job_name => v_des_username||'_IMP',
                                    version =>  'COMPATIBLE');
    DBMS_DATAPUMP.METADATA_FILTER(handle=>v_handle, name=>'SCHEMA_EXPR', value=>'='''||v_src_username||'''', object_path=>NULL);
        dbms_datapump.metadata_filter
        (
            handle => v_handle,
            name => 'EXCLUDE_PATH_EXPR',
            value => q'[ = 'STATISTICS']'
        );
        dbms_datapump.add_file(handle=>v_handle, filename=>v_logfilename,directory=>p_directory,filetype=>DBMS_DATAPUMP.KU$_FILE_TYPE_LOG_FILE);
        dbms_datapump.add_file(handle=>v_handle, filename=>v_dumpfilename,directory=>p_directory,filetype=>DBMS_DATAPUMP.KU$_FILE_TYPE_DUMP_FILE, reusefile=>0);
        dbms_datapump.metadata_remap(handle=>v_handle, name=>'REMAP_SCHEMA', old_value=>v_src_username, value=>v_des_username);
    if (p_src_tbs1 <>'-' and p_des_tbs1<>'-') then
        dbms_datapump.metadata_remap(handle=>v_handle, name=>'REMAP_TABLESPACE', old_value=>p_src_tbs1, value=>p_des_tbs1);
    end if;
    if (p_src_tbs2 <>'-' and p_des_tbs2<>'-') then
        dbms_datapump.metadata_remap(handle=>v_handle, name=>'REMAP_TABLESPACE', old_value=>p_src_tbs2, value=>p_des_tbs2);
    end if;
    if (p_src_tbs3 <>'-' and p_des_tbs3<>'-') then
        dbms_datapump.metadata_remap(handle=>v_handle, name=>'REMAP_TABLESPACE', old_value=>p_src_tbs3, value=>p_des_tbs3);
    end if;
    dbms_datapump.metadata_transform(handle=>v_handle, name=>'OID', value=>0);
    dbms_datapump.metadata_transform(handle=>v_handle, name=>'LOB_STORAGE', value=>'SECUREFILE');
    dbms_datapump.start_job(handle=>v_handle);
        -- Wait for the job to finish...
        -- trovato soluzione pi snella con dbms_datapump.wait_for_job
        DBMS_DATAPUMP.WAIT_FOR_JOB (
                handle => v_handle,
                job_state => l_state);
    :dp_job_state := l_state;                  
    dbms_datapump.detach(handle=>v_handle);
    --copy logfile to common name file
    UTL_FILE.FCOPY (
        src_location    => p_directory,
        src_filename    => v_logfilename,
        dest_location   => p_directory,
        dest_filename   => 'py_dp.log',
        start_line      => 1,
        end_line        => NULL);
    end;"""