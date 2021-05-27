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
from .sql.g_plsql_write_file_on_dir import g_plsql_write_file_on_dir
from .sql.g_plsql_write_mreti_on_dir import g_plsql_write_mreti_on_dir
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
def uploadMultipleBlobStream(p_connection, p_type, *argv):
    """
    this function my be used for load mreti/mareeistat cvs or datapump dumps
    must be called passing dbconnection, string 'mreti' or 'dump' and optionally an abosolute path to locate files to load
    es: uploadMultipleBlobStream(['mydb','mreti',r'c:\tmp\filestoload'])
    """
    con = p_connection
    p_mreti_or_dump = 'mreti'
    if (p_type in ('mreti','dump')):
        p_mreti_or_dump = p_type
    if (len(argv) >  0):
        working_folder = argv[0]
    else:
        working_folder = input("Enter full path for the working folder/directory: ")
    #os.chdir(working_folder)
    #filenames_list = os.listdir()
    filenames_list = []
    findcsv(working_folder, filenames_list)
    #you can filter too, if you need so:
    #filenames_list = [filename for filename in os.listdir() if '.csv' in filename]
    print(filenames_list)
    #mretiConnectString = os.getenv('MRETI_FACTORY1_DB_CONNECT')
    #print(mretiConnectString)
    #con = cx_Oracle.connect(mretiConnectString)
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
        cur.execute("DELETE FROM BLOBFILES")
        cur.execute("""
            insert into blobfiles (dump_name, dump_file, log_file_name, log_file, notes, datetime, id)
            values (:1, empty_blob(), :2, empty_blob(), :3, sysdate, blobfiles_seq.nextval)
            returning dump_file, log_file into :4, :5""", [file, l_log_file_name, l_notes, lobVar, loglobVar])
        #assign element from list:
        blob, = lobVar.getvalue()
        #print(blob)
        offset = 1
        numBytesInChunk = 65536
        
        if (p_mreti_or_dump == 'mreti'):
            with open(file, 'rb') as f:
                while True:
                    data = f.read(numBytesInChunk)
                    #### !!! DOS2UNIX !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ####
                    #################  TO CHANGE FOR MANAGE BOTH DATAPUMP DUMPS AND CSVs   ###################################################
                    #data.replace(b'\r\n', b'\n')
                    if data:
                        blob.write(data.replace(b'\r\n', b'\n'), offset)
                    if len(data) < numBytesInChunk:
                        break
                    offset += len(data.replace(b'\r\n', b'\n'))        
            print("Files uploaded to BLOBs table")
            l_plsql_code = g_plsql_write_mreti_on_dir.replace(':p_file_name',"'"+file+"'")
        elif (p_mreti_or_dump == 'dpdump'):
            with open(file, 'rb') as f:
                while True:
                    data = f.read(numBytesInChunk)
                    if data:
                        blob.write(data, offset)
                    if len(data) < numBytesInChunk:
                        break
                    offset += len(data)        
            print("Files uploaded to BLOBs table")
            l_plsql_code =  g_plsql_write_file_on_dir.replace(':p_file_name',"'"+file+"'")   
        con.commit()
        #print(l_plsql_code)
        cur.execute(l_plsql_code)
        print("Blobs unloaded to DIRECTORY")    
    cur.execute("DELETE FROM BLOBFILES")
    con.commit()
    cur.close()
    #con.close()

#if __name__ == "__main__":
#   uploadMultipleBlobStream(sys.argv[1:])