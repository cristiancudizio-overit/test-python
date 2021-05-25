#https://blogs.oracle.com/oraclemagazine/perform-plsql-operations-with-cx_oracle
#C:\Development-cri\test-python\test-python>oracle_dp_export.py -d expdpuser/ExpDpUser01#@//svil-oracle-19/svil193p1.overit.it -u SVIL910GEOCALL -p DPDIR -f test_exp_py.dpdmp
import sys
import getopt
import os
from datetime import datetime, date, time
import cx_Oracle
import getpass


def oracle_dp_import(argv):
    v_dbstring = 'username/password@//hostname/servicename'
    v_username = 'username'
    v_dumpfilename='x'
    v_directory='DATA_PUMP_DIR'
    v_src_username=''
    v_des_username=''
    v_src_tbs1='-'
    v_des_tbs1='-'
    v_src_tbs2='-'
    v_des_tbs2='-'
    v_src_tbs3='-'
    v_des_tbs3='-'
    l_generate_only = False
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hgd:u:f:p:s:t:",["help","dbstring=","username=","dumpfilename=","directory=","source=","target="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbstring -u username [-f dumpfilename -p directory ...] ')
         print(sys.argv[0]+' -g -u username [-f dumpfilename -p directory ...] --> GENERATE ONLY PL/SQL code')
         sys.exit()
      elif opt in ("-d", "--dbstring"):
          if arg!='':
              v_dbstring = arg
      elif opt in ("-u", "--username"):
          if arg!='':
              v_username = arg
      elif opt in ("-f", "--dumpfilename"):
          if arg!='':
              v_dumpfilename = arg
      elif opt in ("-p", "--directory"):
          if arg!='':
              v_directory = arg
      elif opt in ("-s", "--source"):
          if arg!='':
              v_src_username = arg
      elif opt in ("-t", "--target"):
          if arg!='':
              v_des_username = arg
      elif opt in ("-g"):
            l_generate_only = True
    if v_des_username=='':
        v_des_username = v_src_username
    
    connectString = os.getenv('UTILITY_DB_CONNECT')
    #conUtil = cx_Oracle.connect(connectString)
    v_query = 'SELECT sf_getastrongpassword() NEWPASSWD FROM DUAL'
    #exportSchemaFiltered(p_username varchar2, p_dumpfilename varchar2 default 'x', p_directory varchar2 default 'DPDIR')
    v_plsql_code = "DECLARE\n"
    v_plsql_code = v_plsql_code+"""
          p_src_username varchar2(30) := '{.p_src_username}'; 
          p_des_username varchar2(30) := '{.p_des_username}';
          p_dumpfilename varchar2(60) := '{.p_dumpfilename}';
          p_directory varchar2(30) := '{.p_directory}';
          p_src_tbs1 varchar2(30) := '{.p_src_tbs1}';
          p_des_tbs1 varchar2(30) := '{.p_des_tbs1}';
          p_src_tbs2 varchar2(30) := '{.p_src_tbs2}';
          p_des_tbs2 varchar2(30) := '{.p_des_tbs2}';
          p_src_tbs3 varchar2(30) := '{.p_src_tbs3}';
          p_des_tbs3 varchar2(30) := '{.p_des_tbs3}';"""
    v_plsql_code = v_plsql_code.replace("{.p_src_username}",v_src_username)
    v_plsql_code = v_plsql_code.replace("{.p_des_username}",v_des_username)
    v_plsql_code = v_plsql_code.replace("{.p_dumpfilename}",v_dumpfilename)
    v_plsql_code = v_plsql_code.replace("{.p_directory}",v_directory)
    v_plsql_code = v_plsql_code.replace("{.p_src_tbs1}",v_src_tbs1)
    v_plsql_code = v_plsql_code.replace("{.p_des_tbs1}",v_des_tbs1)
    v_plsql_code = v_plsql_code.replace("{.p_src_tbs2}",v_src_tbs2)
    v_plsql_code = v_plsql_code.replace("{.p_des_tbs2}",v_des_tbs2)
    v_plsql_code = v_plsql_code.replace("{.p_src_tbs3}",v_src_tbs3)
    v_plsql_code = v_plsql_code.replace("{.p_des_tbs3}",v_des_tbs3)
    v_plsql_code = v_plsql_code+"""
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
        end;
    """
    v_ddl_external_table = """
        create table dp_log_et 
           (
          textline    VARCHAR2(256)
        )
           organization external (
           type oracle_loader
           default directory {.directory}
           access parameters (
           records delimited by newline
           CHARACTERSET AL32UTF8
           BADFILE 'dp_log_et.bad'
           LOGFILE 'dp_log_et.log'
           skip 0
           fields terminated by ";" optionally enclosed by "'"
           MISSING FIELD VALUES ARE NULL
           (
                textline
           )
           )
           location
           (
           'py_dp.log'
           )
        )"""
    
    v_ddl_external_table = v_ddl_external_table.replace("{.directory}",v_directory)
    print(v_plsql_code)
    if l_generate_only:
        exit()
    v_risposta = input('des_username: '+v_des_username+' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    con = cx_Oracle.connect(v_dbstring)
    cur = con.cursor()    
    v_dp_job_state = cur.var(str)
    cur.execute(v_plsql_code, dp_job_state=v_dp_job_state)
    #print('JOB STATUS: '+v_dp_job_state.getValue())
    print("STATE: {}".format(v_dp_job_state.getvalue()))
    try:
        cur.execute(v_ddl_external_table)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
    v_query_log = "select textline from dp_log_et"
    cur.execute(v_query_log)
    #scarica tutto il resultset che in questo caso è 1 record
    result = cur.fetchall()
    v_num_rows = cur.rowcount
    v_num_cols = len(cur.description)
    v_description_length = len(cur.description)
    for i in range(v_description_length):
        print(cur.description[i][0])
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_log_line = result[i][j]
            print(v_log_line)
    print('')
    print('DATABASE: '+v_dbstring.split("@",1)[1][2:])
    print('USERNAME: '+v_username)
    
if __name__ == "__main__":
   oracle_dp_import(sys.argv[1:])
    
