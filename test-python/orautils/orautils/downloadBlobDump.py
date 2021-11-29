from datetime import datetime,date
import cx_Oracle
import getpass
import os
import getopt
import sys
from .setup_db import setup_db
from .sql.g_plsql_load_blob_from_dir import g_plsql_load_blob_from_dir
from . import connectionfactory
#v_password = getpass.getpass()
 #h argument without parameter, i: parameter with argument, o: parameter with argumenti
#ifile longoptions
def downloadBlobDump(argv):
    l_log_file_name = ''
    l_dump_name = ''
    l_directory = 'DATA_PUMP_DIR'
    opts, args = getopt.getopt(argv,"hd:f:l:p:",["help","dbstring=","dumpfilename=", "logfilename=", "directory="])    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(sys.argv[0]+' -d dbstring -f dumpfilename [-p directory (default DATA_PUMP_DIR)...] ')
            sys.exit()
        elif opt in ("-d", "--dbstring"):
            if arg!='':
                l_dbstring = arg
        elif opt in ("-f", "--dumpfilename"):
            if arg!='':
                l_dump_name = arg
        elif opt in ("-l", "--logfilename"):
            if arg!='':
                l_log_file_name = arg
        elif opt in ("-p", "--directory"):
            if arg!='':
                l_directory = arg
    v_risposta = input('Dumpfilename: '+l_dump_name+' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    #con = cx_Oracle.connect(l_dbstring)
    con = connectionfactory.getdbconnection(l_dbstring)
    cursor = con.cursor()
    setup_db(cursor)
    l_plsql_code = g_plsql_load_blob_from_dir
    l_plsql_code = l_plsql_code.replace(':p_dumpfilename', "'"+l_dump_name+"'")
    l_plsql_code = l_plsql_code.replace(':p_logfilename', "'"+l_log_file_name+"'")
    l_plsql_code = l_plsql_code.replace(':p_directory', "'"+l_directory+"'")
    print(l_plsql_code)
    cursor.execute(l_plsql_code)
    con.commit()
    print("Files uploaded as BLOBs")
    cursor.execute("select dump_name, dump_file, log_file_name, log_file from blobfiles where dump_name = :1 order by datetime desc", [l_dump_name])
    dump_name, dump_file, log_file_name, log_file = cursor.fetchone()
    offset = 1
    num_bytes_in_chunk = 65536
    with open(dump_name, "wb") as f:
        while True:
            data = dump_file.read(offset, num_bytes_in_chunk)
            if data:
                f.write(data)
            if len(data) < num_bytes_in_chunk:
                break
            offset += len(data)
    offset = 1
    num_bytes_in_chunk = 65536
    if (log_file_name != None):
        with open(log_file_name, "wb") as f:
            while True:
                data = log_file.read(offset, num_bytes_in_chunk)
                if data:
                    f.write(data)
                if len(data) < num_bytes_in_chunk:
                    break
                offset += len(data)        
    cursor.close()
    con.close()       
    print("Files downloaded locally") 
if __name__ == "__main__":
   downloadBlobDump(sys.argv[1:])