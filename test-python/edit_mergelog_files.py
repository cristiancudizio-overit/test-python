import shutil
from datetime import datetime, date, time
#to do and to see
#https://docs.python.org/3/library/os.html
#os.putenv(key, value)
# to execute at least part of the commands
#https://docs.python.org/3/library/subprocess.html#module-subprocess
def prepend_file(p_tf):
    tfnew ='temporary.txt'
    #shutil.copy(p_tf,p_tf+'bck')
    f = open(p_tf,'r')
    fnew = open(tfnew,'w+')
    readed_lines = f.readlines();
    rev_from = readed_lines[4]
    rev_to = readed_lines[5]
    rev_to_splitted = rev_to.split("=")
    print(p_tf+' -> '+rev_to_splitted[1])
    fnew.write('%s' %d)
    fnew.write('\n')
    for i in range(1,12):
        if i == 4:
            fnew.write('set REV_FROM='+rev_to_splitted[1])
        else:
            fnew.writelines(readed_lines[i])
    fnew.write('\n\n----\n')
    fnew.writelines(readed_lines)
    f.close()
    fnew.close()
    shutil.copy(tfnew,p_tf)
d = datetime.today() 
tflist= 'merge_log_list.txt'
flist = open(tflist,'r')
readed_lines = flist.readlines()
for line in readed_lines:
    prepend_file(line[:-1])

