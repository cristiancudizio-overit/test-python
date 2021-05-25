from datetime import datetime,date
import cx_Oracle
import getpass
#v_password = getpass.getpass()
v_query = 'SELECT RIZOCAP,RIZOISTAT,DATASTAMP,RIZOID_MARE,RIZOINIZIO fROM RISTATZONE  WHERE RIZOID_AZON=:RIZOID_AZON'
v_query2 = 'SELECT MAREID,MAREISTCAP,MARECAP,MAREISTAT,MAREXCOORD fROM MAREEISTAT_Q1_20_RUSSIA  WHERE MAREID=:MAREID'
#v_query += '
v_arraysize_s = 100
con = cx_Oracle.connect('geocall/geoWWF#coll@//rds-whirlpoolwfm.coll.aws.dhub.geocall.cloud/whircoll')
con1 = cx_Oracle.connect('geocall/geoWWF#coll@//rds-whirlpoolwfm.coll.aws.dhub.geocall.cloud/whircoll')
con2 = cx_Oracle.connect('geocall/geoWWF#coll@//rds-whirlpoolwfm.coll.aws.dhub.geocall.cloud/whircoll')
con3 = cx_Oracle.connect('geocall/geoWWF#coll@//rds-whirlpoolwfm.coll.aws.dhub.geocall.cloud/whircoll')
cur = con.cursor()
cur1 = con1.cursor()
cur2 = con2.cursor()
cur3 = con3.cursor()
v_arraysize = v_arraysize_s*10
cur.arraysize=v_arraysize
cur1.arraysize=v_arraysize
cur2.arraysize=v_arraysize
cur3.arraysize=v_arraysize
#print(cur.arraysize)
v_start = datetime.now().strftime("%M:%S.%f")
print(v_start);
for v_loopindex in range(1000,2000,9):
    cur.execute(v_query, RIZOID_AZON=v_loopindex)
#    cur1.execute(v_query)
    cur2.execute(v_query2, MAREID=v_loopindex)
    cur3.execute(v_query2, MAREID=v_loopindex-1)
    # scarica tutto il resultset
    result = cur.fetchall()
#    result1 = cur1.fetchall()
    result2 = cur2.fetchall()
    result3 = cur3.fetchall()
    v_num_rows = cur.rowcount;
    v_num_cols = len(cur.description)
    #
    v_dest_file_name='test_exp_xxx.txt'
    #f_dst = open(v_dest_file_name,'w')
    v_endquery = datetime.now().strftime("%M:%S.%f")
    print(v_endquery);
    v_description_length = len(cur.description)
    for i in range(v_description_length):
        v_test2= cur.description[i][0]
#    for i in range(v_num_rows):
#        for j in range(v_num_cols):
#            v_test = result[i][j]
#            if isinstance(v_test, cx_Oracle.Timestamp):
#                v_test = v_test.strftime("%M:%S.%f")  
    #f_dst.close()
    v_endscan = datetime.now().strftime("%M:%S.%f")
    #print(str(v_arraysize)+'\t '+str(v_start)+' '+str(v_endquery)+' '+str(v_endscan));
#v_oggi = date.today().strftime("%Y%m%d")
cur.close()
con.close()
cur1.close()
con1.close()
cur2.close()
con2.close()
cur3.close()
con3.close()  