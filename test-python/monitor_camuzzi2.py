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
query = query + 'select * from xmonalerts'
query = query + ' where idsnapshot=(select max(coalesce(id,0)) from xmonsnapshots)'
cur = con.cursor()
cur.prepare(query)
#cur.execute(None, {'diskc': '%C:%','diske': '%E:%'})
while (1==1):
    cur.execute(None)
    res = cur.fetchall()
    #res = cur.fetchmany(numRows=1)
    #print(res)
    #print(len(res))
    #print(cur.description)
    #for r in res:
    #    print(r)
    #    print(len(r))
    #print(res[1][2])    
    # hide main window
    root = tkinter.Tk(screenName='screen_name',baseName='base_name')
    #root.withdraw()
    # message box display
    #messagebox.showinfo("ora version",con.version)
    #msg = tkinter.Message(root, text=con.version)
    #msg.config(bg='lightgreen',font=('times',24,'italic'), width=1250)
    #msg.pack()
    root.title('Titolo')
    #button = tkinter.Button(root, text='Ok', width=25, command=root.iconify)
    button = tkinter.Button(root, text='Ok', width=25, command=root.destroy)
    button.pack()
    text = tkinter.Text(root, height=30, width=140)
    text.pack()
    text.insert(tkinter.END, 'XMONALERT')
    text.insert(tkinter.END, '\n')
    toaster = ToastNotifier()
    alert = 'false'
    for r in res:
        print(str(r[1])+' '+str(r[2]))
        if (str(r[2]) != 'NONE'):
            alert = 'true'
            toaster.show_toast(str(r[1]),
                       str(r[2]),
                       icon_path="refresh16.ico",
                       duration=3,
                        threaded=True)
            text.insert(tkinter.END, str(r[1])+' '+str(r[2])+' '+str(r[4])+' '+str(r[6])+'\n')
            #tkinter.messagebox
            #root.mainloop()
            #root.update()
            #root.update_idletasks()
            #time.sleep(60)
            #print('after mainloop')
    if (alert == 'true'):
        root.mainloop()
    time.sleep(600)
    #root.destroy()
cur.close()
con.close()



