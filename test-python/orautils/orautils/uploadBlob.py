from datetime import datetime,date
import cx_Oracle
import getpass
#v_password = getpass.getpass()
con = cx_Oracle.connect('root/uu8EpWJ1fkEWEwb@//rds-factory-01.prod.d-hub.aws.overit.it/factory1')
cur = con.cursor()
with open('example.txt', 'r') as f:
    textdata = f.read()

#with open('image.png', 'rb') as f:
#    imgdata = f.read()

cursor.execute("""insert into lob_tbl (id, c)
               values (:lobid, :clobdata)""",
        lobid=10, clobdata=textdata)
con.commit()
cur.close()
con.close()
