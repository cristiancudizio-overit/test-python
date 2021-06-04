import cx_Oracle
import os
connectStrings = {}
connectStrings['GEOCTEST'] = 'ROOT_GEOCTEST_DB_CONNECT'
connectStrings['GEOCDEMO'] = 'ROOT_GEOCDEMO_DB_CONNECT'
connectStrings['FACTORY1'] = 'ROOT_FACTORY1_DB_CONNECT'
connectStrings['FACTORY3'] = 'ROOT_FACTORY3_DB_CONNECT'
connectStrings['MRETI_FACTORY1'] = 'MRETI_FACTORY1_DB_CONNECT'
connectStrings['FACTORY4'] = 'ROOT_FACTORY4_DB_CONNECT'
connectStrings['GP01PROD'] = 'ROOT_GP01PROD_DB_CONNECT'
connectStrings['GP03PROD'] = 'ROOT_GP03PROD_DB_CONNECT'
connectStrings['WINDTRETEST'] = 'ROOT_WINDTRETEST_DB_CONNECT'
connectStrings['UTILITY_FACTORY1'] = 'UTILITY_DB_CONNECT'
def getDBConnectionString(p_dbstring):
    if (p_dbstring.count('@')==1):
        return p_dbstring.split("@",1)[1][2:]
    else:
        return os.getenv(connectStrings.get(p_dbstring.upper())).split("@",1)[1][2:]  
def getdbconnection(p_dbstring):
    l_test_connection = 'NONE'
    if (p_dbstring.count('@')==1):
        try:
            con = cx_Oracle.connect(p_dbstring)
            l_test_connection = 'CONNECTED'
        except cx_Oracle.DatabaseError as e:
            l_test_connection = 'FAILED'
    else:
        if connectStrings.get(p_dbstring.upper()) == None:
            print("Available DBTARGETS: ")
            for i in connectStrings:
                print('- ',i)
            print("---------")
            print(' DB TARGET NOT FOUND, EXITING')
            exit()
    if (l_test_connection == 'FAILED'):
        print('DB CONNECTION FAILED, EXITING')
        exit()
    elif (l_test_connection != 'CONNECTED'):
        v_dbstring = os.getenv(connectStrings.get(p_dbstring.upper()))
        con = cx_Oracle.connect(v_dbstring)
    return con