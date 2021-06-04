import os
import sys, getopt
from orautils.orautils import password_manager
def main(argv):
    inputfile = 'c:/oracle/accessi_db.txt'
    opts, args = getopt.getopt(argv,"hi:o:",["ifile="])    
    for opt, arg in opts:
       if opt == '-h':
             print(sys.argv[0]+' -i <inputfile>')
             sys.exit()
       elif opt in ("-i", "--ifile"):
            if arg!='':
                inputfile = arg
       if opt == '-o':
            conn_string = arg
    print('Input file is "', inputfile)
    inputfile='c:/oracle/accessi_db.txt'
    flist = open(inputfile,'r')
    flist_readed_lines = flist.readlines()
    flist.close()
    for line in flist_readed_lines:        
            if not line.strip().startswith('#'):
                #parse line to get info:
                line_items = line.strip().split('/')
                #print(os.environ['TNS_ADMIN'])
                #print(os.environ)
                #print('sqlplus '+line_items[0]+'/'+line_items[1]+'@'+line_items[2])
                #print(line_items[2].strip())
                #print(conn_string.strip())
                if (line_items[2].strip() == conn_string.strip()):
                    os.system('sqlplus '+line_items[0]+'/'+line_items[1]+'@'+line_items[2])  
def test(argv):
      v_pwd = password_manager.getElement(argv)
      os.system('sql root/'+v_pwd+'@//rds-windtre.test.aws.dhub.geocall.cloud/windtre')  
if __name__ == "__main__":
   test(sys.argv[1:])
