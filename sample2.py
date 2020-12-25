from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter import *
def proces():
    number1=Entry.get(E1)
    number2=Entry.get(E2)
    operator=Entry.get(E3)
    number1=int(number1)
    number2=int(number2)
    if operator =="+":
        answer=number1+number2
    if operator =="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    Entry.insert(E4,0,answer)
    print(answer)

top = tkinter.Tk()
L1 = Label(top, text="My Simple Calculator",).grid(row=0,column=1)
L2 = Label(top, text=" Enter Number 1",).grid(row=1,column=0)
L3 = Label(top, text=" Enter Number 2",).grid(row=2,column=0)
L4 = Label(top, text="Enter Operator (+,-, *,/)",).grid(row=3,column=0)

E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=5,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=4,column=1,)
L4 = Label(top, text="Answer",).grid(row=5,column=0)

#code for Opening File
 
top.geometry('600x500')
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(): 
    file = filedialog.askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
btn = Button(top, text ='Open File', command = lambda:open_file()) 

# Re program


def callback():
    if mb.askyesno('Verify', 'Really want to Re-Program ?'):
        btn.grid(row=1, column=3)
    else:
        mb.showinfo('No', 'Re-Program has been cancelled')

tk.Button(text='Do you want to Re Program this Simple Calculator?', command=callback).grid(row=8, column=4)
tk.mainloop()
  
#mainloop() 

top.mainloop()


                                  
