import cx_Oracle
import tkinter
from tkinter import messagebox
from win10toast import ToastNotifier
import time
#https://pythonspot.com/tk-message-box/
#https://www.geeksforgeeks.org/python-gui-tkinter/
##
con = cx_Oracle.connect('expdpuser/expdpuser@//svil-oracle-12/svil121p1.overit.it')
print(con.version)
query = ''
query = query + 'select * from xmonalerts order by id desc'
cur = con.cursor()
cur.prepare(query)
#cur.execute(None, {'diskc': '%C:%','diske': '%E:%'})
while (1==1):
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
    
    #msg = tkinter.Message(root, text=con.version)
    #msg.config(bg='lightgreen',font=('times',24,'italic'), width=1250)
    #msg.pack()
    root.title('Titolo')    
    toaster = ToastNotifier()
    for r in res:
        print(str(r[1]))
        if (str(r[2]) != 'NONE'):            
            toaster.show_toast(str(r[1]),
                       str(r[2]),
                       icon_path="refresh16.ico",
                       duration=3,
                        threaded=True)
            messagebox.showinfo(str(r[1]),str(r[2]))
    #        text.insert(tkinter.END, str(r[1])+' '+str(r[2])+' '+str(r[4])+' '+str(r[6])+'\n')
    
    #tkinter.messagebox        
    #root.mainloop()
    time.sleep(600)
cur.close()
con.close()



