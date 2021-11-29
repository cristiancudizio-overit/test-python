#https://towardsdatascience.com/stop-using-print-to-debug-in-python-use-icecream-instead-79e17b963fcc

import subprocess
import shutil
import sys
import getopt
import os
from datetime import datetime, date, time
import cx_Oracle
import getpass
from . import connectionfactory
from .init_rds_config import init_rds_config
from .init_rds_config import _init_rds_config
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
def drop_oracle_rds_user(argv):
    v_dbtarget = 'geoctest'
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

    connUtil = connectionfactory.getdbconnection('UTILITY_FACTORY1')
    v_query = "SELECT * FROM AWSRDSDATABASELIST where schema=upper(:username)"
    v_data = {"username": v_username}
    curUtil = connUtil.cursor()
    curUtil.execute(v_query, v_data)
    result = curUtil.fetchall()
    v_num_rows = curUtil.rowcount
    v_num_cols = len(curUtil.description)
    v_description_length = len(curUtil.description)
    for i in range(v_description_length):
        #print(curUtil.description[i][0])
        pass
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_col_value = result[i][j]
            print("{0:30}:{}".format(curUtil.description[j][0], v_col_value))
    curUtil.close()
    connUtil.close()
def create_oracle_rds_user(argv):
    v_dbtarget = 'geoctest'
    #v_dbstring = 'username/password@//hostname/servicename'
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

    connUtil = connectionfactory.getdbconnection('UTILITY_FACTORY1')
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
    if v_tablespaces == '':
        v_tablespace_list = [v_prefix+'GEODATA', v_prefix+'GEOINDX', v_prefix+'GEOLOB']
    v_tablespace_list_full = v_tablespace_list.copy()
    print('')
    print(v_dbtarget)
    print('DATABASE: '+connectionfactory.getDBConnectionString(v_dbtarget))
    print('USERNAME: '+v_username)
    print('PASSWORD: '+v_newpassword)
    for i_tbs in v_tablespace_list_full:
            print('TABLESPACE: '+i_tbs)
    print('TEST CONNECTION: sql '+v_username+'/'+v_newpassword+'@//'+connectionfactory.getDBConnectionString(v_dbtarget))
    v_risposta = input('username: '+v_username+' prefix: '+v_prefix+ 'Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    con = connectionfactory.getdbconnection(v_dbtarget)
    # if the db is new it needs some startup configuration
    _init_rds_config(con)
    cur = con.cursor()            
    for i_tbs in v_tablespace_list:
            create_tablespace(i_tbs, cur)
    v_query =  'CREATE USER '+v_username+' IDENTIFIED BY "'+v_newpassword+'" '
    v_query += 'DEFAULT TABLESPACE  '+v_tablespace_list[0]+' QUOTA UNLIMITED ON '+v_tablespace_list[0]
    v_tablespace_list.pop(0)
    for i_tbs in v_tablespace_list:
        v_query += ' QUOTA UNLIMITED ON '+i_tbs
    v_query += ' PROFILE GEOCALL_PROFILE'
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
    #save info into table AWSRDSDATABASELIST at utility@//rds-factory-01.prod.d-hub.aws.overit.it/factory1
    v_oggi = date.today().strftime("%d/%m/%Y")
    v_queryC = 'INSERT INTO AWSRDSDATABASELIST '
    v_queryC += '(schema, password, destination, project_prefix, activation_date, aws_tenant, full_connection_string)'
    v_queryC += ' VALUES '
    v_queryC += ' (upper(:username), :password, :destination, :project_prefix, :activation_date, '
    v_queryC += ' :aws_tenant,:username||\'/\'||:password||\'@//\'||:destination) '
    v_data = {"username": v_username, "password": v_newpassword, "destination": connectionfactory.getDBConnectionString(v_dbtarget),
              "project_prefix": v_prefix, "activation_date": v_oggi, "aws_tenant": v_namespace}
    #print(v_queryC)
    curUtil.execute(v_queryC, v_data)
    connUtil.commit()
    curUtil.close()
    connUtil.close()
    v_dbstring_new = v_username+'/'+v_newpassword+'@//'+connectionfactory.getDBConnectionString(v_dbtarget)
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
    
def get_connection_string(argv):
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hu:",["help","user="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -u username')
         sys.exit()
      elif opt in ("-u", "--username"):
          if arg!='':
              v_username = arg

    connUtil = connectionfactory.getdbconnection('UTILITY_FACTORY1')
    curUtil = connUtil.cursor()
    v_query = 'SELECT * from AWSRDSDATABASELIST where schema like :schema'
    v_data = {"schema": '%'+v_username.upper()+'%'}
    curUtil.execute(v_query, v_data)
    result = curUtil.fetchall()
    v_num_rows = curUtil.rowcount
    v_num_cols = len(curUtil.description)
    v_description_length = len(curUtil.description)
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_col_value = result[i][j]
            print("{0:30}:{1}".format(curUtil.description[j][0], v_col_value))


    v_query = 'SELECT full_connection_string from AWSRDSDATABASELIST where schema like :schema'
    v_data = {"schema": '%'+v_username.upper()+'%'}
    #print(v_queryC)
    curUtil = connUtil.cursor()
    curUtil.execute(v_query, v_data)
    #scarica tutto il resultset 
    result = curUtil.fetchall()
    v_num_rows = curUtil.rowcount
    v_num_cols = len(curUtil.description)
    v_description_length = len(curUtil.description)
    for i in range(v_description_length):
        print(curUtil.description[i][0])
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_full_connection_string = result[i][j]
            print(v_full_connection_string)    
if __name__ == "__main__":
   create_oracle_rds_user(sys.argv[1:])
    
