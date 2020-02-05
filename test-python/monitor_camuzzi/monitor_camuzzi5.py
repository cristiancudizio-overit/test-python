#!/usr/bin/python3
import cx_Oracle
import tkinter
from tkinter import messagebox
from win10toast import ToastNotifier
import time
#https://pythonspot.com/tk-message-box/
#https://www.geeksforgeeks.org/python-gui-tkinter/
##
while (1==1):
    try: 
        con = cx_Oracle.connect('expdpuser/expdpuser@//svil-oracle-12/svil121p1.overit.it')
        print(con.version)
        query = ''
        query = query + 'select * from xmonalerts'
        query = query + ' where idsnapshot=(select max(coalesce(id,0)) from xmonsnapshots)'
        #cur.execute(None, {'diskc': '%C:%','diske': '%E:%'})
        root = tkinter.Tk(screenName='screen_name',baseName='base_name')
        root.title('root Titolo')
        # hide main window
        #root.withdraw()
        button = tkinter.Button(root, text='Ok', width=25, command=root.destroy)
        #button = tkinter.Button(root, text='Ok', width=25, command=root.iconify)
        button.pack()
        text = tkinter.Text(root, height=30, width=140)
        text.pack()
        text.insert(tkinter.END, 'XMONALERT')
        text.insert(tkinter.END, '\n')
        toaster = ToastNotifier()
        while (1==1):
            cur = con.cursor()
            cur.prepare(query)
            cur.execute(None)
            res = cur.fetchall()
            # message box display
            #messagebox.showinfo("ora version",con.version)
            #msg = tkinter.Message(root, text=con.version)
            #msg.config(bg='lightgreen',font=('times',24,'italic'), width=1250)
            #msg.pack()
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
                #se viene chiuso occorre reinizializzare tutto
                root = tkinter.Tk(screenName='screen_name',baseName='base_name')
                root.title('root Titolo')
                # hide main window
                #root.withdraw()
                button = tkinter.Button(root, text='Ok', width=25, command=root.destroy)
                #button = tkinter.Button(root, text='Ok', width=25, command=root.iconify)
                button.pack()
                text = tkinter.Text(root, height=30, width=140)
                text.pack()
                text.insert(tkinter.END, 'XMONALERT')
                text.insert(tkinter.END, '\n')
            time.sleep(600)
            #root.destroy()
            cur.close()
            #break ? if root closed?
    except cx_Oracle.Error as N:
        print(N)
con.close()



