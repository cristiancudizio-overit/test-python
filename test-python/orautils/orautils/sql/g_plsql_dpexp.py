g_plsql_dpexp_tables = """DECLARE
    p_username varchar2(30) := :p_username;
    p_dumpfilename varchar2(40) := :p_dumpfilename;
    p_directory varchar2(40) := :p_directory;
    p_postfix varchar2(40) := :p_postfix;
    p_version varchar2(30) := 'COMPATIBLE';
    -- ver 1.1 
    -- date: 28/05/2021
    v_handle number;
    v_logfilename varchar2(40);
    v_dumpfilename varchar2(40);
    v_username varchar2(30);
    l_state varchar2(30) := 'NONE';
    l_status ku$_status;
    begin
    v_username := upper(p_username);
    p_postfix := upper(p_postfix);
    if (p_dumpfilename='x') then
        v_dumpfilename := v_username||'.dpdmp';
    else
        v_dumpfilename := p_dumpfilename;
    end if;
    v_logfilename  := 'exp_'||substr(v_dumpfilename,1,length(v_dumpfilename)-6)||'.log';
    begin 
    v_handle := dbms_datapump.open( operation => 'EXPORT', 
                                    job_mode =>'TABLE', 
                                    job_name => v_username||'_EXP',
                                    version =>  p_version);
    DBMS_DATAPUMP.METADATA_FILTER(handle=>v_handle, name=>'SCHEMA_EXPR', value=>'='''||v_username||'''', object_path=>NULL);                                    
    DBMS_DATAPUMP.METADATA_FILTER(handle=>v_handle, name=>'NAME_EXPR', value=>'LIKE ''%'||p_postfix||'''', object_path=>NULL);
    dbms_datapump.add_file(handle=>v_handle, filename=>v_logfilename,directory=>p_directory,filetype=>DBMS_DATAPUMP.KU$_FILE_TYPE_LOG_FILE);
    dbms_datapump.add_file(handle=>v_handle, filename=>v_dumpfilename,directory=>p_directory,filetype=>DBMS_DATAPUMP.KU$_FILE_TYPE_DUMP_FILE, reusefile=>1);
    dbms_datapump.start_job(handle=>v_handle);
    -- Wait for the job to finish...
    --
    DBMS_DATAPUMP.WAIT_FOR_JOB (
        handle => v_handle,
        job_state => l_state);
    -- l_state out parameter "STOPPED" or "COMPLETED"
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
    --exception when others then 
    --dbms_datapump.detach(handle=>v_handle);
    --raise;
    end;
    end;"""
g_plsql_dpexp = """DECLARE
    p_username varchar2(30) := :p_username;
    p_dumpfilename varchar2(40) := :p_dumpfilename;
    p_directory varchar2(40) := :p_directory;
    p_version varchar2(30) := 'COMPATIBLE';
    -- ver 1.1 
    -- date: 27/05/2021
    -- backport p_version
    -- date: 08/10/2020
    -- https://docs.oracle.com/database/121/ARPLS/d_datpmp.htm#ARPLS66033
    -- test: exec exportSchemaFiltered(p_username=>'SVIL900DEMOGEOCALL');
    v_handle number;
    v_logfilename varchar2(40);
    v_dumpfilename varchar2(40);
    v_username varchar2(30);
    l_state varchar2(30) := 'NONE';
    l_status ku$_status;
    begin
    v_username := upper(p_username);
    if (p_dumpfilename='x') then
        v_dumpfilename := v_username||'.dpdmp';
    else
        v_dumpfilename := p_dumpfilename;
    end if;
    v_logfilename  := 'exp_'||substr(v_dumpfilename,1,length(v_dumpfilename)-6)||'.log';
    begin 
    v_handle := dbms_datapump.open( operation => 'EXPORT', 
                                    job_mode =>'SCHEMA', 
                                    job_name => v_username||'_EXP',
                                    version =>  p_version);
    DBMS_DATAPUMP.METADATA_FILTER(handle=>v_handle, name=>'SCHEMA_EXPR', value=>'='''||v_username||'''', object_path=>NULL);
    --DBMS_DATAPUMP.SET_PARAMETER(handle => v_handle, name => 'COMPRESSION', value => 'ALL' );
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'SLOG', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'SCOLLEGAMENTI', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'RLASTSYNCREPLICHEPDA', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'PCACHEREPLICAPDA', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'SIMPORTEXPORTMASTER', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'SIMPORTEXPORTRIGHE', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'SERRORIWEBSERVICES', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'SSINCRONIZZAZIONEPDA', schema_name => v_username);
    --DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'XWFMSPOSIZIONIGPSUTENTE', schema_name => v_username);

    -- DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'ARISORSE', schema_name => v_username);
    -- DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'XWFMSODLRIGHE', schema_name => v_username);
    -- DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'XWFMSODLTESTATE', schema_name => v_username);
    -- DBMS_DATAPUMP.DATA_FILTER(handle => v_handle, name => 'SUBQUERY', value => ' WHERE 1=0 ', table_name  => 'SSCHEDARACCOLTADATI', schema_name => v_username);
    dbms_datapump.add_file(handle=>v_handle, filename=>v_logfilename,directory=>p_directory,filetype=>DBMS_DATAPUMP.KU$_FILE_TYPE_LOG_FILE);
    dbms_datapump.add_file(handle=>v_handle, filename=>v_dumpfilename,directory=>p_directory,filetype=>DBMS_DATAPUMP.KU$_FILE_TYPE_DUMP_FILE, reusefile=>1);
    dbms_datapump.start_job(handle=>v_handle);
    -- Wait for the job to finish...
    --
    DBMS_DATAPUMP.WAIT_FOR_JOB (
        handle => v_handle,
        job_state => l_state);
    -- l_state out parameter "STOPPED" or "COMPLETED"
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
    --exception when others then 
    --dbms_datapump.detach(handle=>v_handle);
    --raise;
    end;
    end;"""