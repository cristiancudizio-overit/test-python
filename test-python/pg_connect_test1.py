#!/usr/bin/python
#https://www.postgresqltutorial.com/postgresql-python/connect/
import psycopg2
#from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(
          host="factory-pg-02.cie8j9fv1zig.eu-west-1.rds.amazonaws.com",
          database="factory",
          user="geocall",
          password="geocall980")
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        cur.execute('SELECT usename,client_addr,state FROM pg_stat_activity WHERE pid = pg_backend_pid()');
        v_client_info = cur.fetchone()
        print(v_client_info)
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
def lambda_handler(event, context):
    connect()
    print('vala')
    return 1

if __name__ == '__main__':
    connect()