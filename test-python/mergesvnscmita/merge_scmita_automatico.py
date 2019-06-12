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
#prepara due file .cmd, uno per il merge e uno per il commit
def create_cmd_file(p_tf):
    tfnew = p_tf[:-4]+'.cmd'
    tfnew_commit = p_tf[:-4]+'_commit.cmd'
    print(tfnew)
    f = open(p_tf,'r')
    fnew = open(tfnew,'w+')
    fnew_commit = open(tfnew_commit,'w+')
    readed_lines = f.readlines();
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
    for i in range(1,11):
        #print(str(i))
        #print(readed_lines[i])
        if i<4:
            fnew.writelines(readed_lines[i])
            fnew_commit.writelines(readed_lines[i])
        elif i == 4:
            fnew.write('set REV_FROM='+rev_from)
            fnew_commit.write('set REV_FROM='+rev_from)
        elif i == 5:
            fnew.write('set REV_TO='+str(rev_to)+'\n')
            fnew_commit.write('set REV_TO='+str(rev_to)+'\n')
        elif i == 7:
            fnew.write('cd '+base_path+'%PROJECT_NAME%-%BRANCH_TO%'+sub_path+'\n')
            fnew_commit.write('cd '+base_path+'%PROJECT_NAME%-%BRANCH_TO%'+sub_path+'\n')
        elif i == 8 or i == 9:
            fnew.writelines(readed_lines[i])
        elif i == 10:
            fnew_commit.write('svn_commit.cmd\n')
        else:
            fnew.writelines(readed_lines[i])
            fnew_commit.writelines(readed_lines[i])
    f.close()
    fnew.close()
    fnew_commit.close()
    return (tfnew,tfnew_commit)
#procedura obsoleta sostituita
def prepend_file_old(p_tf):
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
#inserisce in testa al file di log l'output dell'ultimo .cmd    
def prepend_file(p_tf):
    tfnew ='temporary.txt'
    tfcmd = p_tf[:-4]+'.cmd'
    fold = open(p_tf,'r')
    #backup per test
    shutil.copy(p_tf,'log\\'+p_tf)
    f = open(tfcmd,'r')
    fnew = open(tfnew,'w+')
    readed_lines = f.readlines();
    for i in range(0,len(readed_lines)):
        fnew.writelines(readed_lines[i])
    fnew.write('\n\n----\n')
    #accoda il contenuto completo del file com'era prima
    readed_lines_old = fold.readlines()
    fnew.writelines(readed_lines_old)
    f.close()
    fold.close()
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
    flist_readed_lines = flist.readlines()
    #passa uno ad uno i file di log del merge.
    for line in flist_readed_lines:        
        if not line.strip().startswith('#'):
            #print(line[:-1])
            cmd_files = create_cmd_file(line[:-1])
            #file cmd che fa il merge
            cmd_file_name = cmd_files[0]
            #file cmd che fa il commit
            cmd_commit_file_name = cmd_files[1]
            #lancia cmd del merge e cattura l'output e lo accoda al file cmd stesso
            cp = subprocess.run(cmd_file_name, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,encoding="cp1252")
            print(cp.stdout)
            #out_file = cmd_file_name[:-4]+'.out'
            fof = open(cmd_file_name,'a+')
            fof.write(cp.stdout)
            v_risposta = 'NO'
            while v_risposta != 'yes' 
                v_risposta = input('continuare (yes/no)? ')
            #se rispondo si lancio il commit
            print(cmd_commit_file_name)
            cp2 = subprocess.run(cmd_commit_file_name, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,encoding="cp1252")
            fof.write(cp2.stdout)                
            fof.close()
            #inserisce in testa al log il contenuto completo del cmd, quindi comandi e output
            prepend_file(line[:-1])
            #sposta file cmd per non avere confusione
            shutil.move(cmd_file_name,'log\\')
            shutil.move(cmd_commit_file_name,'log\\')
    flist.close()
if __name__ == "__main__":
   main(sys.argv[1:])

