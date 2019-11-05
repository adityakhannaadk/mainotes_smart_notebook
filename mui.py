import mainotes as mn
import tkinter    
from tkinter import *
import ttk

f = open('notes.txt', "r+")

lines = f.readlines()  
#Entry fields note fields searches

master = Tk()
def entry_field():
    
  root = Tk()
  root.iconbitmap(default=r'C:\Users\Vikas\OneDrive\Pictures\Discord\mainotes.ico')
  text = Text(root)
  text.insert(INSERT, mn.search_final(0.2,lines,E1.get()))
  text.pack()
  print(mn.search_final(0.2,lines,E1.get())) 
   
def note_field():
  global f 
  global lines
  f.write(E1.get()+" \n")   
  f.close()
  f = open('notes.txt', "r+")
  lines = f.readlines()  



E1 = Entry(master, bg='#36393f',bd=4.493,relief='flat')
E1.pack(side = RIGHT)


#Bt = ttk.Button(master, text='Search', bg = "black", style='Fun.TButton',command=entry_field)
Bt = Button(master,bg='#36393f',fg='#00a2e8',text='Search',relief='flat',command=entry_field)
Bt.pack(side=LEFT)

Bt = Button(master,bg='#36393f',fg='#00a2e8',text='Note',relief='flat',command=note_field)
Bt.pack(side=RIGHT)








master.mainloop()
