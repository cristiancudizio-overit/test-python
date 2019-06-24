import subprocess
import shutil, sys, getopt, os
from datetime import datetime, date, time
import svn.local

v_oggi = date.today().strftime("%Y%m%d")
print(v_oggi)
os.mkdir('log')
shutil.move('log','log_'+v_oggi)
