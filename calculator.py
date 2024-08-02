from tkinter import *
import tkinter.messagebox
from tkinter.constants import SUNKEN
 
root =Tk()
root.title("-------Calculator-------")
frame =Frame(master=root, bg="black", padx=10)
frame.pack()
entry = Entry(master=frame, borderwidth=3, width=53)
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=3) 
 
def input_value(number):
    entry.insert(END, number)
 
 
def equal():
    try:
        a = str(eval(entry.get()))
        entry.delete(0,END)
        entry.insert(0, a)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
 
 
def clear():
    entry.delete(0,END)
 
 
button_1 = Button(master=frame, text='1', padx=15,pady=5, width=5, command=lambda: input_value(1))
button_1.grid(row=1, column=1, pady=2)
button_2 = Button(master=frame, text='2', padx=15,pady=5, width=5, command=lambda: input_value(2))
button_2.grid(row=1, column=2, pady=2)
button_3 =Button(master=frame, text='3', padx=15,pady=5, width=5, command=lambda: input_value(3))
button_3.grid(row=1, column=3, pady=2)
button_4 = Button(master=frame, text='4', padx=15,pady=5, width=5, command=lambda: input_value(4))
button_4.grid(row=2, column=1, pady=2)
button_5 = Button(master=frame, text='5', padx=15,pady=5, width=5, command=lambda: input_value(5))
button_5.grid(row=2, column=2, pady=2)
button_6 = Button(master=frame, text='6', padx=15,pady=5, width=5, command=lambda: input_value(6))
button_6.grid(row=2, column=3, pady=2)
button_7 = Button(master=frame, text='7', padx=15,pady=5, width=5, command=lambda: input_value(7))
button_7.grid(row=3, column=1, pady=2)
button_8 = Button(master=frame, text='8', padx=15,pady=5, width=5, command=lambda: input_value(8))
button_8.grid(row=3, column=2, pady=2)
button_9 = Button(master=frame, text='9', padx=15,pady=5, width=5, command=lambda: input_value(9))
button_9.grid(row=3, column=3, pady=2)
button_0 = Button(master=frame, text='0', padx=15,pady=5, width=5, command=lambda: input_value(0))
button_0.grid(row=4, column=2, pady=2)

button_dot= Button(master=frame, text='.', padx=15,pady=5, width=5, command=lambda: input_value('.'))
button_dot.grid(row=6, column=2, pady=2)
 
button_add = Button(master=frame, text="+", padx=15,pady=5, width=5, command=lambda: input_value('+'))
button_add.grid(row=1, column=0, pady=2)
 
button_subtract = Button(master=frame, text="-", padx=15, pady=5, width=5, command=lambda: input_value('-'))
button_subtract.grid(row=2, column=0, pady=2)
 
button_multiply = Button(master=frame, text="*", padx=15, pady=5, width=5, command=lambda: input_value('*'))
button_multiply.grid(row=3, column=0, pady=2)
 
button_div = Button(master=frame, text="/", padx=15,pady=5, width=5, command=lambda: input_value('/'))
button_div.grid(row=4, column=0, pady=2)

button_openbracket = Button(master=frame, text="(", padx=15,pady=5, width=5, command=lambda: input_value('('))
button_openbracket.grid(row=6, column=0, pady=2)

button_closebracket = Button(master=frame, text=")", padx=15,pady=5, width=5, command=lambda: input_value(')'))
button_closebracket.grid(row=6, column=1, pady=2)

 
button_clear = Button(master=frame, text="clear",padx=15, pady=5, width=20, command=clear)
button_clear.grid(row=7, column=1, columnspan=2, pady=2)
 
button_equal = Button(master=frame, text="=", padx=15,pady=5, width=5, command=equal)
button_equal.grid(row=6, column=3,pady=2)
 
root.mainloop()




