#https://blogs.oracle.com/oraclemagazine/perform-plsql-operations-with-cx_oracle
#C:\Development-cri\test-python\test-python>oracle_dp_export.py -d expdpuser/ExpDpUser01#@//svil-oracle-19/svil193p1.overit.it -u SVIL910GEOCALL -p DPDIR -f test_exp_py.dpdmp
import sys
import getopt
import os
from datetime import datetime, date, time
import cx_Oracle
import getpass
from .sql.g_plsql_dpimp import g_plsql_dpimp
from .sql.g_sql_ddl_external_table_dplog import g_sql_ddl_external_table_dplog
from .sql.g_sql_ddl_external_table_dplog import g_sql_drop_external_table_dplog
from  . import connectionfactory
def oracle_dp_import(argv):
    """esempio d'uso:
    python -m orautils oracle_dp_import -d root/xxxxxx@//rds-factory-03.prod.d-hub.aws.overit.it/factory  -f geocalleletropaulo_pre_20210420.dpdmp -s geocalleletropaulo -t SVIL823ENELSAOPAULO -r geodata:edrgeodata,geoindx:edrgeoindx,geolob:edrgeolob
    """
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
    v_tablespace_remap = ''
    v_tablemode = 'no'
    v_table_name = ''
    v_table_exists_action = 'SKIP'
    v_tablespace_remap = list()
    for i in range(len(v_tablespace_remap),3):
                    v_tablespace_remap.append('-:-')
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hgmd:u:f:p:s:t:r:n:x:",["help","generateonly","tablemode","dbstring=","username=","dumpfilename=","directory=","source=","target=","remap_tablespace=","tablename","tableexistsaction"])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbstring -s sourceschema -t targetschema -f dumpfilename -r srctbs:destbs, [-m for table mode -p directory ... -n tablename -x TRUNCATE, REPLACE, APPEND, and SKIP.] ')
         print(sys.argv[0]+' -g -u username [-f dumpfilename -p directory ...] --> GENERATE ONLY PL/SQL code')
         sys.exit()
      elif opt in ("-m", "--tablemode"):
           v_tablemode = 'yes'
      elif opt in ("-d", "--dbstring"):
          if arg!='':
              v_dbstring = arg
      elif opt in ("-u", "--username"):
          if arg!='':
              v_username = arg.upper()
      elif opt in ("-f", "--dumpfilename"):
          if arg!='':
              v_dumpfilename = arg
      elif opt in ("-p", "--directory"):
          if arg!='':
              v_directory = arg
      elif opt in ("-s", "--source"):
          if arg!='':
              v_src_username = arg.upper()
      elif opt in ("-t", "--target"):
          if arg!='':
              v_des_username = arg.upper()
      elif opt in ("-n", "--tablename"):
          if arg!='':
              v_table_name = arg.upper()
      elif opt in ("-x", "--tableexistsaction"):
          if arg!='':
              v_table_exists_action = arg.upper()
      elif opt in ("-r", "--remap_tablespace"):
          if arg!='':
              v_tablespace_remap =  list(element for element in arg.upper().split(','))
              for i in range(len(v_tablespace_remap),3):
                    v_tablespace_remap.append('-:-')
              print(v_tablespace_remap)
      elif opt in ("-g"):
            l_generate_only = True
    if v_des_username=='':
        v_des_username = v_src_username
    con = connectionfactory.getdbconnection(v_dbstring)
    v_plsql_code = g_plsql_dpimp
    v_plsql_code = v_plsql_code.replace("{.p_src_username}",v_src_username.upper())
    v_plsql_code = v_plsql_code.replace("{.p_des_username}",v_des_username.upper())
    v_plsql_code = v_plsql_code.replace("{.p_dumpfilename}",v_dumpfilename)
    v_plsql_code = v_plsql_code.replace("{.p_directory}",v_directory.upper())
    v_plsql_code = v_plsql_code.replace("{.p_table_name}",v_table_name.upper())
    v_plsql_code = v_plsql_code.replace("{.p_table_exists_action}",v_table_exists_action.upper())
    for i in range(len(v_tablespace_remap)):
        v_plsql_code = v_plsql_code.replace("{.p_src_tbs"+str(i+1)+"}",v_tablespace_remap[i].split(':')[0])
        v_plsql_code = v_plsql_code.replace("{.p_des_tbs"+str(i+1)+"}",v_tablespace_remap[i].split(':')[1])
    if (v_tablemode == 'yes'):
       v_plsql_code = v_plsql_code.replace("job_mode =>'SCHEMA',","job_mode =>'TABLE',")
    if (v_table_name != ''):
        v_plsql_code = v_plsql_code.replace("--TABLE_NAME--","")
    v_ddl_external_table = g_sql_ddl_external_table_dplog    
    v_ddl_external_table = v_ddl_external_table.replace("{.directory}",v_directory)
    v_drop_external_table = g_sql_drop_external_table_dplog
    print(v_plsql_code)
    if l_generate_only:
        exit()
    v_risposta = input('des_username: '+v_des_username+' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        con.close()
        exit()
    cur = con.cursor()    
    v_dp_job_state = cur.var(str)
    cur.execute(v_plsql_code, dp_job_state=v_dp_job_state)
    #print('JOB STATUS: '+v_dp_job_state.getValue())
    print("STATE: {}".format(v_dp_job_state.getvalue()))
    try:
        cur.execute(v_drop_external_table)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
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
    #print('DATABASE: '+v_dbstring.split("@",1)[1][2:])
    print('DATABASE: '+v_dbstring)
    print('USERNAME: '+v_des_username)
    
if __name__ == "__main__":
   oracle_dp_import(sys.argv[1:])
    
