import string
from tkinter import *
from tkinter import messagebox as mb
import random
from datetime import datetime
# collecting characters

A=string.ascii_uppercase
a=string.ascii_lowercase
pun=string.punctuation
numbers=string.digits
# _______________________________________________________
def Gen_password():
    c_list=[]

    c_list.extend(list(a))
    c_list.extend(list(A))
    c_list.extend(list(pun))
    c_list.extend(list(numbers))
    try:
        lan=int(var.get())
    except Exception as e:
        mb.showinfo("Error","Enter a intager")
    random.shuffle(c_list)
    global password
    password=("".join(c_list[0:lan]))

    var2.set(password)
    return password


def copy():
    file=open("PassWord logs.txt","a")
    now = datetime.now()
    dt_string = now.strftime("Date------->"+"%B %d,%Y "+"Time------>"+"%H:%M:%S")
    root.clipboard_clear()
    root.clipboard_append(password)
    file.write(f'Password----->  {password}  ----->{dt_string}\n')
    file.close()


root=Tk()
root.geometry("250x170")
root.resizable(0,0)
root.title("PassWord generator")


var=StringVar()
var2=StringVar()

inputLable=Label(root,text="Enter the length of your password",pady=5).grid(row=1,column=1)
inputEntry=Entry(root,textvariable=var).grid(row=2,column=1,ipadx=10,pady=5)

button1=Button(root,text="Get password", relief=RAISED,pady=0,command=Gen_password).grid(row=3,column=1)


output=Label(root,text="output",pady=10,fg="red",font="bold").grid(row=4,column=1)
outputEntry=Entry(root,textvariable=var2).grid(row=5,column=1,ipadx=10)
button2=Button(root,text="Copy", relief=RAISED,pady=0,command=copy).grid(row=5,column=2)



root.mainloop()