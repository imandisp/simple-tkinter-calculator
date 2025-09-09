import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Calculator")
root.geometry("300x400")

#display frame
frame1=ttk.Frame(root)
frame1.pack()
entry=ttk.Entry(frame1,font="arial 20",width=16)
entry.pack(pady=20)

#button frame
frame2=ttk.Frame(root)
frame2.pack()

buttons=[("7",0,0),("8",0,1),("9",0,2),("/",0,3),("4",1,0),("5",1,1),("6",1,2),("*",1,3),("1",2,0),("2",2,1),("3",2,2),("-",2,3),("0",3,0),("C",3,1),("=",3,2),("+",3,3)]

def clear():
    entry.delete(0,tk.END)

def calculate(event=None):
    try:
        ans=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")

def click_button(value):
    entry.insert(tk.END,value)

def backspace(event=None):
    entry.delete(len(entry.get())-1,tk.END)

def press_key(event):
    character=event.char
    if character.isdigit() or character in "+-*/":
        entry.insert(tk.END,character)
    
for btn in buttons:
    if btn[0]=="C":
        action=clear
    elif btn[0]=="=":
        action=calculate
    else:
        action=lambda x=btn[0]: click_button(x)

    button=tk.Button(frame2,text=btn[0],width=9,height=4,command=action)
    button.grid(row=btn[1],column=btn[2],sticky="nsew")

root.bind("<Return>",calculate)
root.bind("<KP_Enter>",calculate)
root.bind("<BackSpace>",backspace)
root.bind("<Key>",press_key)

root.mainloop()

#test