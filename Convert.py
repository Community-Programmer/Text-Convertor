from tkinter import *

root=Tk()
root.resizable(False,False)
root.title("TEXT CONVERTOR BY COMMUNITY PROGRAMMER")

def convert():
    global b
    a=text1.get("1.0",END)
    text1.delete("1.0",END)
    b=a.upper()
    text1.insert("1.0",b)

def copy():
    b=text1.get("1.0",END)
    text1.clipboard_clear()
    text1.clipboard_append(b)

def remove():
    text1.delete("1.0",END)

text1=Text(root,font=("Arial",15),height=5,width=60)
text1.grid(columnspan=3)

button1=Button(root,text="CONVERT NOW",font=("Georgia",15),bg="lightblue",command=convert)
button1.grid(ipadx=20)

copy=Button(root,text="COPY TO CLIPBOARD",font=("Georgia",15),command=copy,bg="lightgreen")
copy.grid(ipadx=40,column=2,row=1)

erase=Button(root,text="ERASE",font=("Georgia",15),bg="#fa8e70",command=remove)
erase.grid(ipadx=40,column=1,row=1)


root.mainloop()