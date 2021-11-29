import shutil
import sys
import getopt
import os
import cx_Oracle
import getpass
from . import connectionfactory
from .sql.g_plsql_init_rds_db import g_plsql_init_rds_db
"""
 Create init db configurazione for geocall installation
"""

def _init_rds_config(con):
    cur = con.cursor() 
    #statement_list = [y.replace(';','') for x in g_plsql_init_rds_db.split('\n') for y in x if y != '' and not y.lstrip().startswith('--')] 
    statement_list = [x.replace(';','') for x in g_plsql_init_rds_db.split('\n') if x !='' and not x.lstrip().startswith('--')]
    for stmt in statement_list:
        try:
            cur.execute(stmt)
            print(stmt)
        except cx_Oracle.DatabaseError as e:
            errorObj, = e.args
            #print("User already exists")
            print("Error Code:", errorObj.code)
            print("Error Message:", errorObj.message)
    cur.close()

def init_rds_config(argv):
    v_dbtarget = 'X'
    v_username = 'username'
    #h argument without parameter, i: parameter with argument, o: parameter with argumenti
    #ifile longoptions
    opts, args = getopt.getopt(argv,"hd:",["help","dbtarget="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget ')
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
    con = connectionfactory.getdbconnection(v_dbtarget)
    _init_rds_config(con)
    con.close()

if __name__ == "__main__":
   init_rds_config(sys.argv[1:])
    
