import xlwt
from datetime import datetime,date
import cx_Oracle
import getpass
v_password = getpass.getpass()
con = cx_Oracle.connect('overitcommesse/'+v_password+'@//prod-oracle-11r2/prod112.overit.it')
cur = con.cursor()
v_query = 'SELECT * fROM ('
v_query += ' select                                                                  '
v_query += ' X10ROCDID,                                                              '
v_query += ' X10ADISID,                                                              '
v_query += ' MAX(X10ROCDID) OVER (PARTITION BY X10ADISID) MAXORDINE,                 '
v_query += ' X10AOCLCODICE CODICE_ORDINE,                                            '
v_query += ' X10AOCLDESCRIZIONE DESCRIZIONE_ORDINE,                                  '
v_query += ' X10AOCLNUMERODISPOSITIVI NUMERO_DISPOSITIVI_ORDINE,                     '
v_query += ' A2.X10AALODESCRIZIONE DESCRIZIONE_CLIENTE_ORDINE,                       '
v_query += ' LSAUDESCRIZIONE,                                                        '
v_query += ' X10ADISCODICE,                                                          '
v_query += ' X10ADISSERIALETELLUS,                                                   '
v_query += ' X10ADISIDSATFINDER,                                                     '
v_query += ' X10ADISIDMEZZO,                                                         '
v_query += ' X10ADISNOTE,                                                            '
v_query += ' X10ASSICODICE CODICE_SIM,                                               '
v_query += ' X10ASSIDESCRIZIONE DESCRIZIONE_SIM,                                     '
v_query += ' X10ASSINUMTELEFONICO NUMERO_TELEFONICO_SIM,                             '
v_query += ' X10AOTEDESCRIZIONE DESC_OPERATORETELEFONICO_SIM,                        '
v_query += ' X10TTANDESCRIZIONE DESC_ANTENNA,                                        '
v_query += ' X10TTDIDESCRIZIONE DESC_DISPOSITIVO ,                                   '
v_query += ' A1.X10AALODESCRIZIONE DESC_PROPRIETARIO_SIM                             '
v_query += ' from                                                                    '
v_query += ' X10ADISPOSITIVI                                                         '
v_query += ' left join X10TTIPODISPOSITIVI on (X10ADISID_X10TTDI = X10TTDIID )       '
v_query += ' left join X10TTIPOANTENNE on (X10ADISID_X10TTAN = X10TTANID)            '
v_query += ' LEFT JOIN X10ASCHEDESIM ON (X10ADISID_X10ASSI = X10ASSIID)              '
v_query += ' LEFT JOIN X10AOPERATORITELEFONICI  ON (X10ASSIID_X10AOTE = X10AOTEID)   '
v_query += ' LEFT JOIN X10AAZIENDELOGISTICA A1 ON (X10ASSIID_X10AALO = A1.X10AALOID) '
v_query += ' LEFT JOIN X10RORDINICLIENTIDISPOSITIVI ON (X10ROCDID_X10ADIS = X10ADISID)'
v_query += ' LEFT JOIN X10AORDINICLIENTI ON (X10ROCDID_X10AOCL = X10AOCLID)'  
v_query += ' JOIN X10AAZIENDELOGISTICA A2 ON (X10AOCLID_X10AALO = A2.X10AALOID)'
v_query += ' LEFT JOIN X10TTIPOORDINI ON (X10AOCLID_X10TTOR = X10TTORID)'
v_query += ' JOIN LSTATIAUTOMA ON (X10AOCLID_LSAU = LSAUID))'
v_query += ' WHERE MAXORDINE = X10ROCDID'
cur.execute(v_query)
# scarica tutto il resultset
result = cur.fetchall()
v_num_rows = cur.rowcount;
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
wb.save('esportazione_tellus_'+v_oggi+'.xls')
