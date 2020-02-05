#!/usr/bin/python3
import cx_Oracle
import tkinter
from tkinter import messagebox
from win10toast import ToastNotifier
import time
from datetime import datetime,date
#https://pythonspot.com/tk-message-box/
#https://www.geeksforgeeks.org/python-gui-tkinter/
##
while (1==1):
    try: 
        con = cx_Oracle.connect('expdpuser/expdpuser@//svil-oracle-12/svil121p1.overit.it')
        print(con.version)
        query = ''
        #query = query + 'select * from xmonalerts'
        #query = query + ' where idsnapshot=(select max(coalesce(id,0)) from xmonsnapshots)'
        #query = query + ' select a.idsnapshot,a.alert_type, a.alert,a.activation_start,s.progetto,s.datastamp,r.file_type,r.percent_space_used from xmonalerts a '
        #query = query + ' join xmonsnapshots s on (a.idsnapshot=s.id) '
        #query = query + ' join xmonrecoveryareausage r on (r.id=s.id) '
        #query = query + ' where a.idsnapshot in (select max(coalesce(id,0)) from xmonsnapshots group by progetto)'
        query = query + 'with a1 as ( '
        query = query + 'select a.idsnapshot,a.alert,a.alert_type,a.activation_start,s.progetto,s.datastamp,r.file_type,r.percent_space_used '
        query = query + 'from xmonalerts a '
        query = query + 'join xmonsnapshots s on (a.idsnapshot=s.id) '
        query = query + 'join xmonrecoveryareausage r on (r.id=s.id) '
        query = query + ' where a.idsnapshot in '
        query = query + ' (select max(coalesce(id,0)) from xmonsnapshots WHERE 1=1 group by progetto) '
        query = query + '), '
        query = query + 'a2 as ( '
        query = query + 'select id,tablespace_name,  fmb fmb_abs, amb, ammb, round(100*(ammb-amb+fmb)/ammb) fmb, '
        query = query + ' row_number() over (partition by id order by (ammb-amb+fmb)/ammb)  rn  '
        query = query + 'from xmontablespaceusage '
        query = query + '), '
        query = query + 'a3 as ( '
        query = query + 'select * from a2 where rn=1 '
        query = query + ') '
        query = query + 'select a1.*,a3.tablespace_name,a3.fmb '
        query = query + 'from a3 join a1 on (a3.id = a1.idsnapshot) '
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
            v_oggi = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            print('---------------- ')
            print(v_oggi)
            print('---------------- \n')
            for r in res:
                print(f'{str(r[4]):15}'+'\t '+str(r[0])+'\t'+str(r[1])+'\t '+str(r[2])+'\t '+str(r[5])+'\t '+str(r[6])+'\t '+str(r[7])+'\t '+f'{str(r[8]):20}'+'\t '+str(r[9]))
                if (str(r[2]) != 'NONE'):
                    print('  ------ !!! ALERT !!! ------ \n')
                    alert = 'true'
                    toaster.show_toast(str(r[0]),
                               str(r[1]),
                               icon_path="refresh16.ico",
                               duration=3,
                                threaded=True)
                    text.insert(tkinter.END, str(r[4])+' '+str(r[0])+' '+str(r[1])+' '+str(r[2])+' '+str(r[5])+' '+str(r[6])+' '+str(r[7])+'\n')
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



