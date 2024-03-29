import xlwt
from datetime import datetime,date
import cx_Oracle
import getpass
from . import connectionfactory

def exportReport2XLS(argv):
    """ 
    export schemas info on xls file
    """
    #v_password = getpass.getpass()
    con = connectionfactory.getdbconnection('UTILITY_FACTORY1')
    cur = con.cursor()
    v_query = 'SELECT  '
    v_query += 'SOURCE, SCHEMA, PASSWORD, '
    #v_query += ' \' sql \'||schema||\'/\'||password||\'@//\'||destination '+','
    v_query += 'FULL_CONNECTION_STRING, '
    v_query += 'DB_INFO, DESTINATION, SIZE_MB, REFERENT,'
    v_query += 'ORDER_ID, ACTIVATION_DATE, OPERATING_HOURS,'
    v_query += 'AWS_TENANT, AWS_ZONE, PROJECT_PREFIX,'
    v_query += 'END_DATE, NOTES'
    v_query += ' FROM AWSRDSDATABASELIST '
    v_query += ' ORDER BY DESTINATION, SCHEMA'
    print(v_query)
    cur.execute(v_query)
    # scarica tutto il resultset
    result = cur.fetchall()
    v_num_rows = cur.rowcount
    v_num_cols = len(cur.description)

    #style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    #    num_format_str='#,##0.00')
    #style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('Foglio1')
    v_description_length = len(cur.description)
    for i in range(v_description_length):
        ws.write(0, i, cur.description[i][0])
    for i in range(v_num_rows):
        for j in range(v_num_cols):
            ws.write(i+1, j, result[i][j])
    cur.close()
    con.close()
    v_oggi = date.today().strftime("%Y%m%d")
    print(v_oggi)
    #ws.write(0, 0, 1234.56, style0)
    #ws.write(1, 0, datetime.now(), style1)
    #ws.write(2, 0, 1)
    #ws.write(2, 1, 1)
    #ws.write(2, 2, xlwt.Formula("A3+B3"))
    wb.save('censimentoRDS_'+v_oggi+'.xls')
