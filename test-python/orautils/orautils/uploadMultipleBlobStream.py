#https://stackoverflow.com/questions/29550290/how-to-open-a-list-of-files-in-python
#from os import listdir
#from os.path import isfile, join
#files_in_dir = [ f for f in listdir('/home/cam/Desktop') if isfile(join('/home/cam/Desktop',f)) ]
##########
from datetime import datetime,date
import cx_Oracle
import getpass
import getopt
import os
import sys
from .setup_db import setup_db
from .sql.g_plsql_write_file_on_dir import g_plsql_write_file_on_dir
from .sql.g_plsql_write_mreti_on_dir import g_plsql_write_mreti_on_dir
from . import connectionfactory
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
    it automatically merges csv files on MRETI.csv o MAREEISTAT.csv file based on the first 4 chars of csv filename excluding path (done in pl/sql code)
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
        #### the delete must be replaced by a key unique for script execution (maybe a timestamp)
        #cur.execute("DELETE FROM BLOBFILES")
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
            ##### the following part must be corrected it doesn't work with complex paths
            l_plsql_code = g_plsql_write_mreti_on_dir.replace(':p_file_name',"'"+file+"'")
        #if this is not an upload of mreti/mareeistat csv files it threats file as binary, it not makes dos2unix nor concatenates files    
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
    #cur.execute("DELETE FROM BLOBFILES")
    con.commit()
    cur.close()

def test():
    mretiConnectString = os.getenv('MRETI_FACTORY1_DB_CONNECT')    
    con = cx_Oracle.connect(mretiConnectString)
    uploadMultipleBlobStream(con, 'mreti')
#todo... needs fullpath cvs filename as parameter    
def writeondirMAREEISTATCSV(argv):
    v_dbtarget = ''
    opts, args = getopt.getopt(argv,"hd:",["help","dbtarget="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget ')
         print("dumps blob MAREEISTAT.csv from  blobfiles table at mreti@factory1 or any other dbtarget specified with -d on directory")
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
    if v_dbtarget == '':
        v_dbtarget =  'MRETI_FACTORY1'
    con = connectionfactory.getdbconnection(v_dbtarget)
    l_plsql_code = g_plsql_write_mreti_on_dir.replace(':p_file_name',"'MAREEISTAT'") ### come secondo parametro ci vorrebbe il full path name...
    print(l_plsql_code)
    cur = con.cursor()
    cur.execute(l_plsql_code)
    cur.close()
def writeondirMRETICSV(argv):
    v_dbtarget = ''
    opts, args = getopt.getopt(argv,"hd:",["help","dbtarget="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget ')
         print("dumps blob MRETI.csv from  blobfiles table at mreti@factory1 or any other dbtarget specified with -d on directory")
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
    if v_dbtarget == '':
        v_dbtarget =  'MRETI_FACTORY1'
    con = connectionfactory.getdbconnection(v_dbtarget)
    ##remember g_plsql_write_mreti_on_dir concatenates all */MRET*???? files into MRETI.csv
    l_plsql_code = g_plsql_write_mreti_on_dir.replace(':p_file_name',"'MRETI'") ### come secondo parametro ci vorrebbe il full path name...
    print(l_plsql_code)
    cur = con.cursor()
    cur.execute(l_plsql_code)
    cur.close()  
def writeFileOnDir(argv):
    v_dbtarget = ''
    v_file_name = ''
    opts, args = getopt.getopt(argv,"hd:f:",["help","dbtarget=","filename="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget ')
         print("dumps blob file specified with -f from  blobfiles table at mreti@factory1 or any other dbtarget specified with -d on directory")
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
      elif opt in ("-f", "--filename"):
          if arg!='':
              v_file_name = arg
    if v_dbtarget == '':
        v_dbtarget =  'MRETI_FACTORY1'
    con = connectionfactory.getdbconnection(v_dbtarget)
    l_plsql_code = g_plsql_write_file_on_dir.replace(':p_file_name',"'"+v_file_name+"'") 
    print(l_plsql_code)
    cur = con.cursor()
    cur.execute(l_plsql_code)
    cur.close()      

def run(argv):
    v_dbtarget = ''
    opts, args = getopt.getopt(argv,"hd:",["help","dbtarget="])    
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print(sys.argv[0]+' -d dbtarget ')
         print("interactively asks you full path of csv files and load on blobfiles table at mreti@factory1 or any other dbtarget specified with -d")
         sys.exit()
      elif opt in ("-d", "--dbtarget"):
          if arg!='':
              v_dbtarget = arg
    if v_dbtarget == '':
        v_dbtarget =  'MRETI_FACTORY1'
    con = connectionfactory.getdbconnection(v_dbtarget)
    #mretiConnectString = os.getenv('MRETI_FACTORY1_DB_CONNECT')    
    #con = cx_Oracle.connect(mretiConnectString)
    uploadMultipleBlobStream(con, 'mreti')
if __name__ == "__main__":
#   uploadMultipleBlobStream(sys.argv[1:])
    test()