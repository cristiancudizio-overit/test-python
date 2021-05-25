import cx_Oracle
def setup_db(p_cur):
    l_query = """create sequence blobfiles_seq"""
    print("SETUP DB ",l_query)
    try:
        p_cur.execute(l_query)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
    l_query = """create table blobfiles (
        id number,
       dump_name varchar2(90), 
       dump_file blob,
       datetime date,
       log_file_name varchar2(90),
       log_file blob,
       notes varchar2(100))"""
    print("SETUP DB ",l_query)
    try:
        p_cur.execute(l_query)
    except cx_Oracle.DatabaseError as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
    #return 'ok'