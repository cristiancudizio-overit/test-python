import shutil, sys, getopt, os
import cx_Oracle
fd = open('extcodes.csv','r')
readed_lines = fd.readlines();
fd.close()
con = cx_Oracle.connect('expdpuser/ExpDpUser01#@//svil-oracle-19/svil193p1.overit.it')
cur = con.cursor()
cur.executemany("""
        insert into ternaextcodes (code)
        values (trim(:1))
        """, [(i,) for i in readed_lines])

con.commit()    
cur.close()
con.close()
