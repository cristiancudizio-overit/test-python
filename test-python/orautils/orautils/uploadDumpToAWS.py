#a sort of fork of uploadMultipleBlobStream
from datetime import datetime,date
import getopt
import sys
import cx_Oracle
import getpass
import os
from .setup_db import setup_db
from .sql.g_plsql_write_file_on_dir import g_plsql_write_file_on_dir
from .sql.g_plsql_write_mreti_on_dir import g_plsql_write_mreti_on_dir
from . import connectionfactory

def _uploadDumpToAWS(p_connection, *argv):
    """
    this function my be used for  datapump dumps
    must be called passing dbconnection,  and optionally an abosolute path to locate files to load
    es: uploadMultipleBlobStream(['mydb',r'c:\tmp\filestoload'])
    """
    con = p_connection
    if (len(argv) >  0):
        working_folder = argv[0]
    else:
        working_folder = input("Enter full path for the working folder/directory: ")
    #os.chdir(working_folder)
    #filenames_list = os.listdir()
    filenames_list = []    
    for entry in os.scandir(working_folder):
        print(working_folder+'\\'+entry.name)
        filenames_list.append(working_folder+os.path.sep+entry.name)
    #os.path.basename(os.path.normpath(filenames_list[0]))
    print(filenames_list)
    cur = con.cursor()
    setup_db(cur)
    for file in filenames_list:
        print(file)
        #print(working_folder+"\\"+file)
        idVal = 1
        lobVar = cur.var(cx_Oracle.BLOB)
        loglobVar = cur.var(cx_Oracle.BLOB)
        l_log_file_name = ''
        l_notes = ''
        l_file_name = os.path.basename(os.path.normpath(file))
        #cur.execute("DELETE FROM BLOBFILES")
        cur.execute("""
            insert into blobfiles (dump_name, dump_file, log_file_name, log_file, notes, datetime, id)
            values (:1, empty_blob(), :2, empty_blob(), :3, sysdate, blobfiles_seq.nextval)
            returning dump_file, log_file into :4, :5""", [l_file_name, l_log_file_name, l_notes, lobVar, loglobVar])
        #assign element from list:
        blob, = lobVar.getvalue()
        #print(blob)
        offset = 1
        numBytesInChunk = 65536
        with open(file, 'rb') as f:
            while True:
                data = f.read(numBytesInChunk)
                if data:
                    blob.write(data, offset)
                if len(data) < numBytesInChunk:
                    break
                offset += len(data)        
        print("Files uploaded to BLOBs table")
        l_plsql_code =  g_plsql_write_file_on_dir.replace(':p_file_name',"'"+l_file_name+"'")   
        con.commit()
        #print(l_plsql_code)
        cur.execute(l_plsql_code)
        print("Blobs unloaded to DIRECTORY")    
    #cur.execute("DELETE FROM BLOBFILES")
    con.commit()
    cur.close()
    #con.close()
def uploadDumpToAWS(argv):
    opts, args = getopt.getopt(argv,"hd:p:",["help", "database=","path="])    
    l_path = r'c:\tmp\MRETI\last'
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(__name__,__package__)
            print(sys.argv[0]+' -d (or --database=) target db -p (or --path=) fullpath of dump files')
            sys.exit()
        elif opt in ("-d", "--database"):
            if arg!='':
                l_dbstring = arg
        elif opt in ("-p", "--path"):
            if arg!='':
                l_path = arg
    v_risposta = input(' Continuare (yes/no)? ')
    if (v_risposta != 'y'):
        print('bye')
        exit()
    con = connectionfactory.getdbconnection(l_dbstring)
    _uploadDumpToAWS(con, l_path)

#if __name__ == "__main__":
#   uploadMultipleBlobStream(sys.argv[1:])
