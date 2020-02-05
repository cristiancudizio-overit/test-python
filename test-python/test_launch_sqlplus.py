import os
import sys, getopt
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
if __name__ == "__main__":
   main(sys.argv[1:])
