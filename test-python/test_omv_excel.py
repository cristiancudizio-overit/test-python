import xlwt
from datetime import datetime,date
import cx_Oracle
import getpass
#v_password = getpass.getpass()
con = cx_Oracle.connect('geocallbi/geocallbi@//161.27.247.149/geocall')
cur = con.cursor()
v_arraysize = 1000
cur.arraysize=v_arraysize
print(cur.arraysize)
v_query = 'SELECT * fROM ASSET  WHERE rownum<100000'
#v_query += '
v_start = datetime.now().strftime("%Y%m%d %H:%M:%S %f")
print(v_start);
cur.execute(v_query)
# scarica tutto il resultset
result = cur.fetchall()
v_num_rows = cur.rowcount;
v_num_cols = len(cur.description)
#
v_endquery = datetime.now().strftime("%Y%m%d %H:%M:%S %f")
print(v_endquery);
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
        #v_test = result[i][j]
cur.close()
con.close()
v_endscan = datetime.now().strftime("%Y%m%d %H:%M:%S %f")
print(str(v_arraysize)+' '+str(v_start)+' '+str(v_endquery)+' '+str(v_endscan));
v_oggi = date.today().strftime("%Y%m%d")
#print(v_oggi)
#ws.write(0, 0, 1234.56, style0)
#ws.write(1, 0, datetime.now(), style1)
#ws.write(2, 0, 1)
#ws.write(2, 1, 1)
#ws.write(2, 2, xlwt.Formula("A3+B3"))
wb.save('esportazione_omv_'+v_oggi+'.xls')
