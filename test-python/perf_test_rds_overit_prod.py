from datetime import datetime,date
import cx_Oracle
import getpass
#v_password = getpass.getpass()
#v_query = 'SELECT * fROM perftestidlist'
v_query = 'SELECT * fROM LCODICECATASTALE'
#v_query += '
v_arraysize_s = 100
for outer_loop_i in range(1,10):
    con = cx_Oracle.connect('sviluppo60/factorydevu03pwd#@//rds-factory-01.prod.d-hub.aws.overit.it/factory1')
    con_selsing = cx_Oracle.connect('sviluppo60/factorydevu03pwd#@//rds-factory-01.prod.d-hub.aws.overit.it/factory1')
    con_ins = cx_Oracle.connect('sviluppo60/factorydevu03pwd#@//rds-factory-01.prod.d-hub.aws.overit.it/factory1')
    cur = con.cursor()
    v_arraysize = v_arraysize_s*1
    cur.arraysize=v_arraysize
    #print(cur.arraysize)
    #v_start = datetime.now().strftime("%M:%S.%f")
    v_start = datetime.now().timestamp()
    #print(v_start);
    cur.execute(v_query)
    # scarica tutto il resultset
    result = cur.fetchall()
    v_num_rows = cur.rowcount;
    v_num_cols = len(cur.description)
    #
    #v_endquery = datetime.now().strftime("%M:%S.%f")
    v_endquery = datetime.now().timestamp()
    #print(v_endquery);
    v_description_length = len(cur.description)
    #nomi colonne
    for i in range(v_description_length):
        v_test2= cur.description[i][0]
        #print(v_test2)
    #scansione valori record    
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_test = result[i][j]
            if isinstance(v_test, cx_Oracle.Timestamp):
                v_test = v_test.strftime("%M:%S.%f")
    cur.close()
    #v_endscan = datetime.now().strftime("%M:%S.%f")
    v_endscan = datetime.now().timestamp()
    #print(str(v_arraysize)+'\t '+str(v_start)+' '+str(v_endquery)+' '+str(v_endscan));
    v_oggi = date.today().strftime("%Y%m%d")
    #test query singole
    cur = con.cursor()
    cur_selsing = con_selsing.cursor()
    cur_ins = con_ins.cursor()
    v_query_selsing = 'SELECT * FROM xbstaclienti WHERE xbstacliid=:xbstacliid'
    v_query_id = 'SELECT * fROM perftestidlist'
    v_query_ins = 'INSERT INTO xbstaclienti_copy (XBSTACLIID, XBSTACLIID_AAZI, XBSTACLICOGNOME, XBSTACLINOME, XBSTACLICODICEFISCALE '
    v_query_ins += ', XBSTACLIDATANASCITA, DATASTAMP, LOGIN, ACTION) VALUES ('
    v_query_ins += ':XBSTACLIID, :XBSTACLIID_AAZI, :XBSTACLICOGNOME, :XBSTACLINOME, :XBSTACLICODICEFISCALE '
    v_query_ins += ', :XBSTACLIDATANASCITA, :DATASTAMP, :LOGIN, :ACTION) '
    cur.execute(v_query_id)
    # scarica tutto il resultset
    result = cur.fetchall()
    v_num_rows = cur.rowcount;
    v_num_cols = len(cur.description)
    #
    v_endquery_id = datetime.now().timestamp()
    #print(v_endquery);
    v_description_length = len(cur.description)
    #nomi colonne
    for i in range(v_description_length):
        v_test2= cur.description[i][0]
        #print(v_test2)
    #scansione valori record    
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            v_test = result[i][j]
        cur_selsing.execute(v_query_selsing, xbstacliid=v_test)
        result_selsing = cur_selsing.fetchall()
        v_num_cols_i = len(cur_selsing.description)
        data = {}
        for i_j in range(v_num_cols_i):
            #ciclo su colonne e faccio dictionary 
            data[":"+cur_selsing.description[i_j][0]] = result_selsing[0][i_j]
        #qui faccio insert singole
        cur_ins.execute(v_query_ins,data)
        con_ins.commit()
    #v_endscan_single = datetime.now().strftime("%M:%S.%f")
    v_endscan_single = datetime.now().timestamp()    
    print(str(v_arraysize)+'\t '+str(v_start)+' '+str(v_endquery)+' '+str(v_endscan)+' '+str(v_endquery_id)+' '+str(v_endscan_single));
    cur.close()
    cur_selsing.close()
    cur_ins.close()
    con.close()
    con_selsing.close()
    con_ins.close()
