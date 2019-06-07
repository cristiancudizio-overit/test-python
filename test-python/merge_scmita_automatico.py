import subprocess
import shutil, sys, getopt
from datetime import datetime, date, time
import svn.local

#to do and to see
#https://docs.python.org/3/library/os.html
#os.putenv(key, value)
# to execute at least part of the commands
#https://docs.python.org/3/library/subprocess.html#module-subprocess
#due parti:
#la prima genera dei singoli file per l'esecuzione corrente
#la seconda esegue i singoli file, cattura l'output e mette tutto in testa
#al file di log originale
#forse conviene separare parte con il commit (per i casi di conflitto...
base_path = '\OVERIT\geocall61\\'
sub_path = '\overit'
def get_svn_rev(p_branch):
    #settare variabili per trovare comando svn... il modulo è solo un wrapper
    r = svn.local.LocalClient(base_path + p_branch + sub_path)
    r.update()
    info = r.info()
    #print(info['entry_revision'] )
    return info['entry_revision']
def get_var_value(p_line):
    line_splitted = p_line.split("=")
    return line_splitted[1]
def create_cmd_file(p_tf):
    #tfnew ='temporary.txt'
    tfnew = p_tf[:-4]+'.cmd'
    print(tfnew)
    f = open(p_tf,'r')
    fnew = open(tfnew,'w+')
    readed_lines = f.readlines();
    #rev_from = readed_lines[4]
    rev_to_old = get_var_value(readed_lines[5])
    rev_from = rev_to_old
    project_name = get_var_value(readed_lines[1])
    branch_to = get_var_value(readed_lines[3])
    rev_to = get_svn_rev(project_name[:-1]+'-'+branch_to[:-1])
    print(p_tf+' -> '+str(rev_from)[:-1]+' '+str(rev_to))
    #prima riga stampa data corrente
    d = datetime.today() 
    fnew.write('REM %s' %d)
    fnew.write('\n')
    #riscrive comandi con revision aggiornate
    #for i in range(1,12):
    # per test si ferma all'update
    for i in range(1,9):
        if i == 4:
            fnew.write('set REV_FROM='+rev_from)
        elif i == 5:
            fnew.write('set REV_TO='+str(rev_to)+'\n')
        elif i == 7:
            fnew.write('cd '+base_path+'%PROJECT_NAME%-%BRANCH_TO%'+sub_path+'\n')
        else:
            fnew.writelines(readed_lines[i])
    f.close()
    fnew.close()
    return tfnew
def prepend_file(p_tf):
    #tfnew ='temporary.txt'
    tfnew = p_tf[:-4]+'.cmd'
    print(tfnew)
    #shutil.copy(p_tf,p_tf+'bck')
    f = open(p_tf,'r')
    fnew = open(tfnew,'w+')
    readed_lines = f.readlines();
    rev_from = readed_lines[4]
    rev_to = readed_lines[5]
    rev_to_splitted = rev_to.split("=")
    print(p_tf+' -> '+rev_to_splitted[1])
    #prima riga stampa data corrente
    fnew.write('%s' %d)
    fnew.write('\n')
    #riscrive comandi con revision aggiornate
    for i in range(1,12):
        if i == 4:
            fnew.write('set REV_FROM='+rev_to_splitted[1])
        else:
            fnew.writelines(readed_lines[i])
    fnew.write('\n\n----\n')
    #accoda il contenuto completo del file com'era prima
    fnew.writelines(readed_lines)
    f.close()
    fnew.close()
    shutil.copy(tfnew,p_tf)
def main(argv):
    inputfile = 'merge_log_list.txt'
    opts, args = getopt.getopt(argv,"hi:o:",["ifile="])    
    for opt, arg in opts:
      if opt == '-h':
         print(sys.argv[0]+' -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
          if arg!='':
              inputfile = arg
    print('Input file is "', inputfile)
    flist = open(inputfile,'r')
    readed_lines = flist.readlines()
    for line in readed_lines:        
        if not line.strip().startswith('#'):
            #print(line[:-1])
            cmd_file_name = create_cmd_file(line[:-1])            
            cp = subprocess.run(cmd_file_name, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,encoding="cp1252")
            print(cp.stdout)
            #out_file = cmd_file_name[:-4]+'.out'
            fof = open(cmd_file_name,'a+')
            fof.write(cp.stdout)
            #prepend_file(line[:-1])
if __name__ == "__main__":
   main(sys.argv[1:])

