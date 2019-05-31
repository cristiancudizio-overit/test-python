import shutil
from datetime import datetime, date, time
d = datetime.today() 
tf = 'textfile.txt'
tfnew = 'textfile2.txt'
shutil.copy(tfnew,tfnew+'bck')
f = open(tf,'r')
fnew = open(tfnew,'w+')
readed_lines = f.readlines();
fnew.write('%s' %d)
fnew.write('\n')
for i in range(0,5):
 fnew.writelines(readed_lines[i])
fnew.write('----\n')
fnew.writelines(readed_lines)
f.close()
fnew.close()
