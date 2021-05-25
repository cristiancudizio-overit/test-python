#https://stackoverflow.com/questions/29550290/how-to-open-a-list-of-files-in-python
#from os import listdir
#from os.path import isfile, join
#files_in_dir = [ f for f in listdir('/home/cam/Desktop') if isfile(join('/home/cam/Desktop',f)) ]
##########
from datetime import datetime,date
import cx_Oracle
import getpass
import os
#v_password = getpass.getpass()
working_folder = input("Enter full path for the working folder/directory: ")
os.chdir(working_folder)
filenames_list = os.listdir()
#you can filter too, if you need so:
filenames_list = [filename for filename in os.listdir() if '.csv' in filename]
print(filenames_list)
con = cx_Oracle.connect('mreti/ciribiribindoman01!@//rds-factory-01.prod.d-hub.aws.overit.it/factory1')
cur = con.cursor()
#with open("MRETI.csv", "rb") as f:

idVal = 1
lobVar = cur.var(cx_Oracle.BLOB)
cur.execute("""
   insert into csvfiles (id, file_name, b)
   values (:1, :2, empty_blob())
   returning b into :3""", [idVal, "xxx", lobVar])
#assign element from list:
blob, = lobVar.getvalue()
#print(blob)
offset = 1
for file in filenames_list:
    print(working_folder+"\\"+file)    
    numBytesInChunk = 65536
    with open(working_folder+"\\"+file, 'rb') as f:
      while True:
        data = f.read(numBytesInChunk)
        if data:
            blob.write(data, offset)
        if len(data) < numBytesInChunk:
            break
        offset += len(data)
con.commit()    
cur.close()
con.close()
