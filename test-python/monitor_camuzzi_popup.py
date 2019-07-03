import cx_Oracle
import time
import tkinter
from tkinter import messagebox
#https://pythonspot.com/tk-message-box/
##
while True:
    con = cx_Oracle.connect('expdpuser/expdpuser@//svil-oracle-12/svil121p1.overit.it')
    print(con.version)
    query = ''
    query = query + 'select * from xmonalerts where activation_start>systimestamp-to_dsinterval(\'00 00:20:00\') '
    query = query + ' and coalesce(activation_end, to_timestamp(\'31-12-2999\',\'dd-mm-yyyy\'))>systimestamp '
    query = query + ' order by id desc'
    cur = con.cursor()
    cur.prepare(query)
    #cur.execute(None, {'diskc': '%C:%','diske': '%E:%'})
    cur.execute(None)
    #res = cur.fetchall()
    res = cur.fetchmany(numRows=1)
    #print(res)
    #print(len(res))
    #print(cur.description)
    #for r in res:
    #    print(r)
    #    print(len(r))
    #print(res[1][2])    
    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    # message box display
    #messagebox.showinfo("ora version",con.version)
    #msg = tkinter.Message(root, text=con.version)
    #msg.config(bg='lightgreen',font=('times',24,'italic'), width=1250)
    #msg.pack()
    for r in res:
        messagebox.showwarning("XXX",str(r[1])+' '+str(r[2])+' '+str(r[4])+' '+str(r[6])+'\n')
        print(str(r[1])) 
    cur.close()
    con.close()
    time.sleep(900)


