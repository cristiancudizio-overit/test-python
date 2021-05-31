#https://stackoverflow.com/questions/29550290/how-to-open-a-list-of-files-in-python
#from os import listdir
#from os.path import isfile, join
#files_in_dir = [ f for f in listdir('/home/cam/Desktop') if isfile(join('/home/cam/Desktop',f)) ]
##########
# da verificare il charset, introdotto dos2unix
from datetime import datetime,date
import cx_Oracle
import getpass
import os

TEST NON AGGIORNATO --> vedere uploadMultipleBlobStream-

# encoding=utf8
os.environ["NLS_LANG"] = "ITALIAN_ITALY.WE8MSWIN1252"
#v_password = getpass.getpass()
working_folder = input("Enter full path for the working folder/directory: ")
os.chdir(working_folder)
filenames_list = os.listdir()
#you can filter too, if you need so:
filenames_list = [filename for filename in os.listdir() if '.csv' in filename]
print(filenames_list)
#con = cx_Oracle.connect('mreti/mreti@//rds-factory-01.prod.d-hub.aws.overit.it/factory1', encoding = "UTF-8")
con = cx_Oracle.connect('mreti/mreti@//rds-factory-01.prod.d-hub.aws.overit.it/factory1')
cur = con.cursor()
#with open("MRETI.csv", "rb") as f:
for file in filenames_list:
    print(working_folder+"\\"+file)
    idVal = 1
    lobVar = cur.var(cx_Oracle.CLOB)
    cur.execute("""
        insert into csvfiles (id, file_name, c)
        values (:1, :2, empty_clob())
        returning c into :3""", [idVal, file, lobVar])
    #assign element from list:
    clob, = lobVar.getvalue()
    #print(blob)
    offset = 1
    numBytesInChunk = 65536
    with open(working_folder+"\\"+file, 'r') as f:
      while True:
        data = f.read(numBytesInChunk)
        data.replace('\r\n', '\n')
        if data:
            clob.write(data, offset)
            #print(data)
        if len(data) < numBytesInChunk:
            break
        offset += len(data)
    con.commit()    
cur.close()
con.close()
