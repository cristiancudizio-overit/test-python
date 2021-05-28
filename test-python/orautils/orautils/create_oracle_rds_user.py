#https://towardsdatascience.com/stop-using-print-to-debug-in-python-use-icecream-instead-79e17b963fcc

import subprocess
import shutil
import sys
import getopt
import os
from datetime import datetime, date, time
import cx_Oracle
import getpass
"create_oracle_rds_module"

def create_tablespace(p_tablespace_name, p_cur):
    l_query = 'create  tablespace '+p_tablespace_name
    print(l_query)
    try:
        p_cur.execute(l_query)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        #print("Tablespace already exists")
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
    #return 'ok'
def create_oracle_rds_user(argv):
    v_dbtarget = 'geoctest'
    v_dbstring = 'username/password@//hostname/servicename'
    v_username = 'username'
    v_prefix = ''
    v_tablespaces = ''
    v_namespace = ''
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hd:u:p:t:n:",["help","dbtarget=","username=","prefix=","tablespaces=","namespace="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget -u username [ -p prefix | -t <comma separaterd tablespace names>] -n <aws tenant>')
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
      elif opt in ("-u", "--username"):
          if arg!='':
              v_username = arg
      elif opt in ("-p", "--prefix"):
          if arg!='-':
              v_prefix = arg
      elif opt in ("-t", "--tablespaces"):
          if arg!='':
              v_tablespaces = arg
              v_tablespace_list =v_tablespaces.split(",")
      elif opt in ("-n", "--namespace"):
          if arg!='':
              v_namespace = arg    
    v_risposta = input('username: '+v_username+' prefix: '+v_prefix+ 'Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    utilityConnectString = os.getenv('UTILITY_DB_CONNECT')
    connUtil = cx_Oracle.connect(utilityConnectString)   
    v_query = 'SELECT sf_getastrongpassword() NEWPASSWD FROM DUAL'
    curUtil = connUtil.cursor()
    curUtil.execute(v_query)
    #scarica tutto il resultset che in questo caso è 1 record
    result = curUtil.fetchall()
    v_num_rows = curUtil.rowcount
    v_num_cols = len(curUtil.description)
    v_description_length = len(curUtil.description)
    for i in range(v_description_length):
        print(curUtil.description[i][0])
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_newpassword = result[i][j]
            print(v_newpassword)
#if you specify -p it will be created three tablespaces <prefix>geo<data,indx,lob>
#if you specify -t it will create tablespaces specified
    con = connectionfactory.getdbconnection(v_dbstring)
    cur = con.cursor()            
    if v_tablespaces == '':
        v_tablespace_list = [v_prefix+'geodata', v_prefix+'geoindx', v_prefix+'geolob']
    for i_tbs in v_tablespace_list:
            create_tablespace(i_tbs, cur)
    v_query =  'CREATE USER '+v_username+' IDENTIFIED BY "'+v_newpassword+'" '
    v_query += 'DEFAULT TABLESPACE  '+v_tablespace_list[0]+' QUOTA UNLIMITED ON '+v_tablespace_list[0]
    v_tablespace_list_full = v_tablespace_list.copy()
    v_tablespace_list.pop(0)
    for i_tbs in v_tablespace_list:
        v_query += ' QUOTA UNLIMITED ON '+i_tbs
    v_query += ' PROFILE GEOCALL_profile'
    print(v_query)
    try:
        cur.execute(v_query)
        print(v_username+" CREATED")
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        #print("User already exists")
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
    v_query = 'GRANT GEOCALL_ROLE TO '+v_username
    print(v_query)
    cur.execute(v_query)
    v_query = 'grant read,write on directory data_pump_dir to '+v_username
    print(v_query)
    cur.execute(v_query)
    cur.close()
    con.close()
    #save info into table censimentodbawsrds at utility@//rds-factory-01.prod.d-hub.aws.overit.it/factory1
    v_oggi = date.today().strftime("%d/%m/%Y")
    v_queryC = 'INSERT INTO censimentodbawsrds '
    v_queryC += '(schema, password, destination, prefix, data_attivazione, aws_tenant, stringa)'
    v_queryC += ' VALUES '
    v_queryC += ' (upper(:username), :password, :destination, :prefix, :data_attivazione, :aws_tenant,:username||\'/\'||:password||\'@//\'||:destination) '
    v_data = {"username": v_username, "password": v_newpassword, "destination": v_dbstring.split("@",1)[1][2:],
              "prefix": v_prefix, "data_attivazione": v_oggi, "aws_tenant": v_namespace}
    #print(v_queryC)
    curUtil.execute(v_queryC, v_data)
    connUtil.commit()
    curUtil.close()
    connUtil.close()
    v_dbstring_new = v_username+'/'+v_newpassword+'@//'+v_dbstring.split("@",1)[1][2:]
    v_query = "SELECT SYSDATE,GLOBAL_NAME FROM GLOBAL_NAME"
    print('Testing connecion to : '+ v_dbstring_new)
    connTest = cx_Oracle.connect(v_dbstring_new)
    curTest = connTest.cursor()
    curTest.execute(v_query)
    #scarica tutto il resultset che in questo caso è 1 record
    result = curTest.fetchall()
    v_num_rows = curTest.rowcount
    v_num_cols = len(curTest.description)
    v_description_length = len(curTest.description)
    for i in range(v_description_length):
        print(curTest.description[i][0])
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_field = result[i][j]
            print(v_field)
    curTest.close()
    connTest.close()
    print('')
    print('DATABASE: '+v_dbstring.split("@",1)[1][2:])
    print('USERNAME: '+v_username)
    print('PASSWORD: '+v_newpassword)
    for i_tbs in v_tablespace_list_full:
            print('TABLESPACE: '+i_tbs)
    print('TEST CONNECTION: sql '+v_username+'/'+v_newpassword+'@//'+v_dbstring.split("@",1)[1][2:])
    
if __name__ == "__main__":
   create_oracle_rds_user(sys.argv[1:])
    
