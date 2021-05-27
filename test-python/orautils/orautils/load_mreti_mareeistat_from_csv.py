from .sql.g_plsql_carica_mreti_mareeistat import g_plsql_carica_mreti_mareeistat
from .sql.g_sql_ddl_mreti_mareeistat_csv import g_sql_ddl_mareeistat_csv
from .sql.g_sql_ddl_mreti_mareeistat_csv import g_sql_ddl_mreti_csv
from .sql.g_sql_ddl_mreti_mareeistat_new import *
from .sql.g_plsql_fremove_files import g_plsql_fremove_mareeistat_csv
from .sql.g_plsql_fremove_files import g_plsql_fremove_mreti_csv
from . import uploadMultipleBlobStream
import cx_Oracle
import sys
import getopt
import os

def _remove_csv_files(p_connection):
    l_cur =p_connection.cursor()
    l_ddl_stmt = g_plsql_fremove_mreti_csv
    try:
        l_cur.execute(l_ddl_stmt)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
        print(l_ddl_stmt)
    l_ddl_stmt = g_plsql_fremove_mareeistat_csv
    try:
        l_cur.execute(l_ddl_stmt)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
        print(l_ddl_stmt)
    l_cur.close()

def _load_mreti_mareeistat_from_csv(p_connection, p_version):
    con = p_connection
    l_version = p_version
    cur = con.cursor()
    ddl_stmt_list = []
    ddl_stmt_list.append('g_sql_ddl_mareeistat_csv')
    ddl_stmt_list.append('g_sql_ddl_mreti_csv')
    ddl_stmt_list.append('g_sql_drop_smareeistat_new')
    ddl_stmt_list.append('g_sql_drop_smreti_new')
    ddl_stmt_list.append('g_sql_drop_mareeistat_new')
    ddl_stmt_list.append('g_sql_drop_mreti_new')
    ddl_stmt_list.append('g_sql_ddl_smareeistat_new')
    ddl_stmt_list.append('g_sql_ddl_mareeistat_new')
    ddl_stmt_list.append('g_sql_ddl_smreti_new')
    ddl_stmt_list.append('g_sql_ddl_mreti_new')
    for i_stmt in ddl_stmt_list:
        #print(globals()[i_stmt])
        l_ddl_stmt = globals()[i_stmt]
        try:
            cur.execute(l_ddl_stmt)
        except cx_Oracle.DatabaseError as e:
            errorObj, = e.args
            print("Error Code:", errorObj.code)
            print("Error Message:", errorObj.message)
            print(l_ddl_stmt)
    l_ddl_stmt = g_plsql_carica_mreti_mareeistat.replace(':p_version',"'"+l_version+"'")
    try:
        cur.execute(l_ddl_stmt)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
        print(l_ddl_stmt)
    
    
def load_mreti_mareeistat_from_csv(argv):
    opts, args = getopt.getopt(argv,"hv:p:",["help", "version=","path="])    
    l_path = r'c:\tmp\MRETI\last'
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(__name__,__package__)
            print(sys.argv[0]+' -v (or --version=) version -p (or --path=) fullpath of csv files')
            sys.exit()
        elif opt in ("-v", "--version"):
            if arg!='':
                l_version = arg
        elif opt in ("-p", "--path"):
            if arg!='':
                l_path = arg
    v_risposta = input(' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    mretiConnectString = os.getenv('MRETI_FACTORY1_DB_CONNECT')    
    con = cx_Oracle.connect(mretiConnectString)
    _remove_csv_files(con)
    uploadMultipleBlobStream.uploadMultipleBlobStream(con, 'mreti', l_path)
    _load_mreti_mareeistat_from_csv(con, l_version)
    _remove_csv_files(con)
    con.close()