#https://stackoverflow.com/questions/29550290/how-to-open-a-list-of-files-in-python
#from os import listdir
#from os.path import isfile, join
#files_in_dir = [ f for f in listdir('/home/cam/Desktop') if isfile(join('/home/cam/Desktop',f)) ]
##########
from datetime import datetime,date
import cx_Oracle
import getpass
import os
from .setup_db import setup_db
from .plsqlcode import *
#v_password = getpass.getpass()
#variable/constant initilized during module import
def findcsv(path, csvfiles):
    """find csvfiles in subtree"""
    for entry in os.scandir(path):
        if  entry.name.endswith('.csv'):
             print(path+'\\'+entry.name)
             csvfiles.append(path+os.path.sep+entry.name)
        elif entry.is_dir():
             findcsv(path+os.path.sep+entry.name, csvfiles)
def uploadMultipleBlobStream(argv):
    working_folder = input("Enter full path for the working folder/directory: ")
    #os.chdir(working_folder)
    #filenames_list = os.listdir()
    filenames_list = []
    findcsv(working_folder, filenames_list)
    #you can filter too, if you need so:
    #filenames_list = [filename for filename in os.listdir() if '.csv' in filename]
    print(filenames_list)
    mretiConnectString = os.getenv('MRETI_FACTORY1_DB_CONNECT')
    print(mretiConnectString)
    con = cx_Oracle.connect(mretiConnectString)
    #con = cx_Oracle.connect('expdpuser/ExpDpUser01#@//svil-oracle-19/svil193p1.overit.it')
    cur = con.cursor()
    setup_db(cur)
    for file in filenames_list:
        print(file)
        #print(working_folder+"\\"+file)
        idVal = 1
        lobVar = cur.var(cx_Oracle.BLOB)
        cur.execute("""
            insert into blobfiles (dump_name, datetime, dump_file)
            values (:1, sysdate, empty_blob())
            returning dump_file into :2""", [file, lobVar])
        #assign element from list:
        blob, = lobVar.getvalue()
        #print(blob)
        offset = 1
        numBytesInChunk = 65536
        with open(file, 'rb') as f:
        #with open(working_folder+"\\"+file, 'rb') as f:
            while True:
                data = f.read(numBytesInChunk)
                #### !!! DOS2UNIX !!!! ####
                #data.replace(b'\r\n', b'\n')
                if data:
                    blob.write(data.replace(b'\r\n', b'\n'), offset)
                if len(data) < numBytesInChunk:
                    break
                offset += len(data.replace(b'\r\n', b'\n'))
        con.commit()
        l_plsql_code = g_plsql_write_mreti_on_dir.replace(':p_file_name',"'"+file+"'")
        #print(l_plsql_code)
        cur.execute(l_plsql_code)
        print("Blobs unloaded to DIRECTORY")    
    con.commit()
    print("Files uploaded to BLOBs")
    #now unload blobs on DIRECTORY
    # maybe i want to cicle on filenames_list
    cur.close()
    con.close()

if __name__ == "__main__":
   uploadMultipleBlobStream(sys.argv[1:])