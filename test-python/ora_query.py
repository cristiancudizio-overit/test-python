import cx_Oracle
con = cx_Oracle.connect('expdpuser/expdpuser@svil-oracle-12/svil121p1.overit.it')
cur = con.cursor()
cur.execute('select fs.*,s.datastamp from xmonfssize fs join xmonsnapshots s on (fs.id=s.id) order by fs.id')
for result in cur:
 print result
cur.close()
con.close()
