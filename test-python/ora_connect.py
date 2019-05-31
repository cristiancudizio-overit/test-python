import cx_Oracle
con = cx_Oracle.connect('expdpuser/expdpuser@svil-oracle-12/svil121p1.overit.it')
print con.version
con.close()
