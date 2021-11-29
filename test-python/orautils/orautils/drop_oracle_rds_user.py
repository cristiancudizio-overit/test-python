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


def drop_oracle_rds_user(argv):
    v_dbtarget = 'geoctest'
    v_username = 'username'
    v_prefix = ''
    v_tablespaces = ''
    v_namespace = ''
    v_notes = ''
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hd:u:n:a:",["help","dbtarget=","username=","namespace=", "notes="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget -u username  -n <aws tenant>')
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
      elif opt in ("-u", "--username"):
          if arg!='':
              v_username = arg
      elif opt in ("-a", "--notes"):
          if arg!='':
              v_notes = arg

    connUtil = connectionfactory.getdbconnection('UTILITY_FACTORY1')
    v_query = "SELECT * FROM AWSRDSDATABASELIST where schema=upper(:username) and DESTINATION=:destination"
    v_data = {"username": v_username, "destination": connectionfactory.getDBConnectionString(v_dbtarget)}
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
            print("{0:30}:{1}".format(curUtil.description[j][0], v_col_value))
            #print(curUtil.description[j][0], v_col_value)
    #curUtil.close()
    #connUtil.close()
    v_risposta = input('username: '+v_username+' target db:'+connectionfactory.getDBConnectionString(v_dbtarget)+ ' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    con = connectionfactory.getdbconnection(v_dbtarget)
    cur = con.cursor()
    v_query = 'DROP USER '+v_username+' CASCADE'
    print(v_query)
    cur.execute(v_query)
    cur.close()
    con.close()
    #save info into table AWSRDSDATABASELIST at utility@//rds-factory-01.prod.d-hub.aws.overit.it/factory1
    v_oggi = date.today().strftime("%d/%m/%Y")
    v_oggi = date.today()
    v_separator = ' - ' 
    v_queryC = 'UPDATE AWSRDSDATABASELIST '
    v_queryC += 'SET end_date = :end_date, '
    v_queryC += 'notes = concat(concat(notes, :separator), :notes)'
    v_queryC += ' WHERE '
    v_queryC += '  SCHEMA=upper(:username) AND DESTINATION=:destination '
    v_data = {"username": v_username, "end_date": v_oggi,  "destination": connectionfactory.getDBConnectionString(v_dbtarget), "notes": v_notes, "separator": v_separator}
    print(v_queryC)
    curUtil.execute(v_queryC, v_data)
    connUtil.commit()
    curUtil.close()
    connUtil.close()
    
    
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
   drop_oracle_rds_user(sys.argv[1:])
    
