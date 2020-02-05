from datetime import datetime,date
import cx_Oracle
import getpass
#v_password = getpass.getpass()
v_query = 'SELECT * fROM ASSET  WHERE rownum<100000'
#v_query += '
v_arraysize_s = 1000
for v_loopindex in range(1,10,1):
    con = cx_Oracle.connect('geocallbi/geocallbi@//161.27.247.149/geocall')
    cur = con.cursor()
    v_arraysize = v_arraysize_s*v_loopindex
    cur.arraysize=v_arraysize
    #print(cur.arraysize)
    v_start = datetime.now().strftime("%M:%S.%f")
    #print(v_start);
    cur.execute(v_query)
    # scarica tutto il resultset
    result = cur.fetchall()
    v_num_rows = cur.rowcount;
    v_num_cols = len(cur.description)
    #
    v_dest_file_name='test_exp_omv.txt'
    f_dst = open(v_dest_file_name,'w')
    v_endquery = datetime.now().strftime("%M:%S.%f")
    #print(v_endquery);
    v_description_length = len(cur.description)
    for i in range(v_description_length):
        v_test2= cur.description[i][0]
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_test = result[i][j]
            if isinstance(v_test, cx_Oracle.Timestamp):
                v_test = v_test.strftime("%M:%S.%f")
    cur.close()
    con.close()
    f_dst.close()
    v_endscan = datetime.now().strftime("%M:%S.%f")
    print(str(v_arraysize)+'\t '+str(v_start)+' '+str(v_endquery)+' '+str(v_endscan));
    v_oggi = date.today().strftime("%Y%m%d")
