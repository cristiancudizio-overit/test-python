#https://blogs.oracle.com/oraclemagazine/perform-plsql-operations-with-cx_oracle
#C:\Development-cri\test-python\test-python>oracle_dp_export.py -d expdpuser/ExpDpUser01#@//svil-oracle-19/svil193p1.overit.it -u SVIL910GEOCALL -p DPDIR -f test_exp_py.dpdmp
import sys
import getopt
import os
from datetime import datetime, date, time
import cx_Oracle
import getpass
from .sql.g_plsql_dpexp import g_plsql_dpexp
from .sql.g_sql_ddl_external_table_dplog import g_sql_ddl_external_table_dplog
from .sql.g_sql_ddl_external_table_dplog import g_sql_drop_external_table_dplog

def oracle_dp_export(argv):
    v_dbstring = 'username/password@//hostname/servicename'
    v_username = 'username'
    v_dumpfilename='x'
    v_directory='DATA_PUMP_DIR'
    l_generate_only = False
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hgd:u:f:p:",["help","dbstring=","username=","dumpfilename=","directory="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbstring -u username [-f dumpfilename -p directory ...] ')
         print(sys.argv[0]+' -g  -u username [-f dumpfilename -p directory ...] --> GENERATE ONLY PL/SQL code')
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
      elif opt in ("-g"):
            l_generate_only = True
    v_risposta = input('username: '+v_username+' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    connectString = os.getenv('UTILITY_DB_CONNECT')
    #conUtil = cx_Oracle.connect(connectString)
    v_query = 'SELECT sf_getastrongpassword() NEWPASSWD FROM DUAL'
    #exportSchemaFiltered(p_username varchar2, p_dumpfilename varchar2 default 'x', p_directory varchar2 default 'DPDIR')
    v_plsql_code = g_plsql_dpexp
    v_plsql_code = v_plsql_code.replace(":p_username","'"+v_username+"'")
    v_plsql_code = v_plsql_code.replace(":p_dumpfilename","'"+v_dumpfilename+"'")
    v_plsql_code = v_plsql_code.replace(":p_directory","'"+v_directory+"'")

    v_drop_external_table = g_sql_drop_external_table_dplog
    v_ddl_external_table = g_sql_ddl_external_table_dplog
    v_ddl_external_table = v_ddl_external_table.replace("{.directory}",v_directory)
    print(v_plsql_code)
    if l_generate_only:
        exit()
    con = cx_Oracle.connect(v_dbstring)
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
    print('DATABASE: '+v_dbstring.split("@",1)[1][2:])
    print('USERNAME: '+v_username)
    
if __name__ == "__main__":
   oracle_dp_export(sys.argv[1:])
    
