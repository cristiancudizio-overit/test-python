import os
import sys, getopt
def main(argv):
    inputfile = 'c:/oracle/accessi_db.txt'
    base_path = os.sep+'ORACLE'+os.sep+'connessionisqlcl'
    putty_path = os.sep+'Users'+os.sep+'ccudizio'+os.sep+'utils'
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
    #inputfile='c:/oracle/accessi_db.txt'
    flist = open(inputfile,'r')
    flist_readed_lines = flist.readlines()
    flist.close()
    for line in flist_readed_lines:        
            if not line.strip().startswith('#'):
                #parse line to get info:
                line_items = line.strip().split('/')
                cmd_file_name = base_path+os.sep+line_items[0]+'_'+line_items[1]+'.cmd'
                cmd_putty_file_name = base_path+os.sep+'putty'+os.sep+line_items[0]+'.cmd'
                cmd_file_handle =open(cmd_file_name,'w+')
                cmd_file_handle.write('call '+base_path+os.sep+'env.cmd \n')
                cmd_file_handle.write('start sql ')
                cmd_file_handle.write(line_items[1]+'/'+line_items[2]+'@'+line_items[0])
                cmd_file_handle.write(' \n')
                cmd_file_handle.close()
                #cmd_putty_file_name = base_path+os.sep+'putty'+os.sep+line_items[0]+'.cmd'
                #cmd_putty_file_handle =open(cmd_putty_file_name,'w+')
                #cmd_putty_file_handle.write(putty_path+os.sep+'PUTTY.EXE ')
                #cmd_putty_file_handle.write('ae48915@'+line_items[3]+' -pw Eneluser13$')
                #os.system('sqlplus '+line_items[0]+'/'+line_items[1]+'@'+line_items[2])    
if __name__ == "__main__":
   main(sys.argv[1:])
