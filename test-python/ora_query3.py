import cx_Oracle
con = cx_Oracle.connect('expdpuser/expdpuser@svil-oracle-12/svil121p1.overit.it')
cur = con.cursor()
cur.prepare('select * from xmonrmanstatus order by id') 
cur.execute(None)
for result in cur:
    print result
cur.prepare('select fs.*,s.datastamp from xmonfssize fs join xmonsnapshots s on (fs.id=s.id) where fs.mount like :mount order by s.datastamp desc')
cur.execute(None, {'mount': '%C:%'})
#for result in cur:
# print result
res = cur.fetchmany(numRows=3)
print res[2][4]
cur.close()
con.close()
