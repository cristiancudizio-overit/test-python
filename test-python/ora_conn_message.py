import cx_Oracle
import tkinter
from tkinter import messagebox
#https://pythonspot.com/tk-message-box/
##
con = cx_Oracle.connect('expdpuser/expdpuser@//svil-oracle-12/svil121p1.overit.it')
print(con.version)
query = ''
query = query + 'select fs.*,s.datastamp '
query = query + 'from xmonsnapshots s join '
query = query + 'xmonfssize fs on (fs.id=s.id) '
query = query + 'where mount like :diskc or mount like :diske '
query = query + 'order by s.datastamp desc,mount desc'
cur = con.cursor()
cur.prepare(query)
cur.execute(None, {'diskc': '%C:%','diske': '%E:%'})
#res = cur.fetchall()
res = cur.fetchmany(numRows=2)
for r in res:
    print(r)
# hide main window
root = tkinter.Tk()
root.withdraw()
# message box display
messagebox.showinfo("ora version",con.version)
cur.close()
con.close()
