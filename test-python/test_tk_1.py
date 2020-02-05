#http://pellacini.di.uniroma1.it/teaching/fondamenti12/lecture12.html
import tkinter as tk
from tkinter import filedialog as fd

FPATH = None

WIN = tk.Tk()
WIN.title('Senza Titolo')
WIN.rowconfigure(0, weight=1)
WIN.columnconfigure(0, weight=1)

TXT = tk.Text(WIN)
TXT.grid(sticky='nsew')

def do_quit():
    WIN.quit()

def do_open():
    path = fd.askopenfilename(title='Scegli un file', 
                              filetypes=[("text", "*.txt"), 
                                         ('python', '*.py')])
    if len(path) > 0:
        global FPATH
        TXT.delete('1.0', 'end')
        with open(path, 'U') as f:
            TXT.insert('1.0', f.read())
        WIN.title(path)
        FPATH = path

def do_saveas():
    path = fd.asksaveasfilename(title='Dove Salvare')
    if len(path) > 0:
        global FPATH
        with open(path, 'w') as f:
            f.write(TXT.get('1.0', 'end'))
        WIN.title(path)
        FPATH = path

def do_save():
    if FPATH != None:
        with open(FPATH, 'w') as f:
            f.write(TXT.get('1.0', 'end'))

mb = tk.Menu(WIN) 
WIN.config(menu=mb)
fm = tk.Menu(mb)
fm.add_command(label='Open...', command=do_open)
fm.add_command(label='Save', command=do_save)
fm.add_command(label='Save As...', command=do_saveas)
fm.add_separator()
fm.add_command(label='Quit', command=do_quit)
mb.add_cascade(label='File', menu=fm)

tk.mainloop()
