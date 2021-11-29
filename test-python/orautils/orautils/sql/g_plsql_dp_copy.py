g_plsql_dp_copy = """
--create or replace procedure duplicateGeocall(
DECLARE
-- ver 1.0.2
-- date: 13/05/2021
-- notes: changed wait_for_job
-- ver 1.0.1 
-- date: 09/06/2020
-- cambio gestione db link selflink
-- ver 1.0 
-- date: 27/04/2018
--    p_src_username varchar2, 
--    p_des_username varchar2, 
--    p_directory varchar2 default 'DPDIR',
--    p_src_tbs1 varchar2 default '-',
--    p_des_tbs1 varchar2 default '-',
--    p_src_tbs2 varchar2 default '-',
--    p_des_tbs2 varchar2 default '-',
--    p_src_tbs3 varchar2 default '-',
--    p_des_tbs3 varchar2 default '-',
--    p_db_link varchar2 default 'SELFLINK'
--) AUTHID CURRENT_USER is
        p_src_username varchar2(30) := '{.p_src_username}'; 
        p_des_username varchar2(30) := '{.p_des_username}';
        p_directory varchar2(30) := '{.p_directory}';
        p_src_tbs1 varchar2(30) := '{.p_src_tbs1}';
        p_des_tbs1 varchar2(30) := '{.p_des_tbs1}';
        p_src_tbs2 varchar2(30) := '{.p_src_tbs2}';
        p_des_tbs2 varchar2(30) := '{.p_des_tbs2}';
        p_src_tbs3 varchar2(30) := '{.p_src_tbs3}';
        p_des_tbs3 varchar2(30) := '{.p_des_tbs3}';
        p_db_link varchar2(100) := '{.p_db_link}';
v_handle number;
v_logfilename varchar2(40);
v_dumpfilename varchar2(40);
v_src_username varchar2(30);
v_des_username varchar2(30);
v_directory varchar2(30);
v_db_link varchar2(60);
l_state varchar2(30) := 'NONE';
l_status ku$_status;
v_version varchar2(30); 
v_compatibility varchar2(30);
begin
dbms_utility.db_version(v_version,v_compatibility);
v_src_username := trim(upper(p_src_username));
v_des_username := trim(upper(p_des_username));
v_directory := upper(p_directory);
v_logfilename  := 'imp_'||v_des_username||'.log';
v_db_link := p_db_link;
if (p_db_link='SELFLINK') then
 select GLOBAL_NAME INTO v_db_link FROM GLOBAL_NAME;
end if;
--begin 
v_handle := dbms_datapump.open( operation => 'IMPORT', 
                                job_mode =>'SCHEMA', 
                                remote_link =>v_db_link,
                                job_name => v_des_username||'_IMP',
                                version =>  'COMPATIBLE');
dbms_output.put_line('src: '||  '='''||v_src_username||'''');                              
DBMS_DATAPUMP.METADATA_FILTER(handle=>v_handle, name=>'SCHEMA_EXPR', value=>'='''||v_src_username||'''', object_path=>NULL);
--DBMS_DATAPUMP.METADATA_FILTER(handle=>v_handle, name=>'SCHEMA_EXPR', value=>'IN ('''||v_src_username||''')', object_path=>NULL);
dbms_datapump.metadata_filter
   (
       handle => v_handle,
       name => 'EXCLUDE_PATH_EXPR',
       value => q'[ = 'STATISTICS']'
   );
dbms_datapump.add_file(handle=>v_handle, filename=>v_logfilename,directory=>v_directory,filetype=>DBMS_DATAPUMP.KU$_FILE_TYPE_LOG_FILE);
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
if (to_number(substr(v_version,1,2))>11 and to_number(substr(v_compatibility,1,2))>11) then
 dbms_datapump.metadata_transform(handle=>v_handle, name=>'DISABLE_ARCHIVE_LOGGING', value=>1);
end if;
dbms_datapump.start_job(handle=>v_handle);
-- Wait for the job to finish...
-- trovato soluzione piu snella con dbms_datapump.wait_for_job
DBMS_DATAPUMP.WAIT_FOR_JOB (
          handle => v_handle,
          job_state => l_state);
:dp_job_state := l_state;
dbms_datapump.detach(handle=>v_handle);
--copy logfile to common name file
UTL_FILE.FCOPY (
    src_location    => v_directory,
    src_filename    => v_logfilename,
    dest_location   => v_directory,
    dest_filename   => 'py_dp.log',
    start_line      => 1,
    end_line        => NULL);
--execute immediate 'alter user '||v_des_username||' identified by '||LOWER(v_des_username);
end;
"""