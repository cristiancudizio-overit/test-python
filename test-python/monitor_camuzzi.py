import cx_Oracle
import tkinter
from tkinter import messagebox
#https://pythonspot.com/tk-message-box/
##
con = cx_Oracle.connect('expdpuser/expdpuser@//svil-oracle-12/svil121p1.overit.it')
print(con.version)
query = ''
query = query + 'select * from xmonalerts order by id desc'
cur = con.cursor()
cur.prepare(query)
#cur.execute(None, {'diskc': '%C:%','diske': '%E:%'})
cur.execute(None)
#res = cur.fetchall()
res = cur.fetchmany(numRows=2)
#print(res)
#print(len(res))
#print(cur.description)
#for r in res:
#    print(r)
#    print(len(r))
#print(res[1][2])    
# hide main window
root = tkinter.Tk()
#root.withdraw()
# message box display
#messagebox.showinfo("ora version",con.version)
#msg = tkinter.Message(root, text=con.version)
#msg.config(bg='lightgreen',font=('times',24,'italic'), width=1250)
#msg.pack()
text = tkinter.Text(root, height=30, width=140)
text.pack()
text.insert(tkinter.END, 'XMONALERT')
text.insert(tkinter.END, '\n')
cur.close()
con.close()
for r in res:
    text.insert(tkinter.END, str(r[1])+' '+str(r[2])+' '+str(r[4])+' '+str(r[6])+'\n')
tkinter.mainloop()

