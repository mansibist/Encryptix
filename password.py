import string
import random
import array
from tkinter import *

window=Tk()
window.title("-----PASSWORD GENERATOR------")
frame=Frame(master=window,bg="skyblue",padx=10)
frame.pack()
text=Label(master=frame,text='Enter the length of the password:',font=('calibri10',30,'bold'),bg="skyblue",fg="black").grid(row=0,column=0)
entry =Entry(master=frame, borderwidth=3, width=10,font=('arial',20,'bold'))
entry.grid(row=0, column=1)

button_generate=Button(master=frame, text='GENERATE PASSWORD',font=('arial',25,'bold'), width=20,command=lambda:password_generator(entry))
button_generate.grid(row=1, column=0)

display = Entry(master=frame, borderwidth=3, width=30,font=('arial',35,'bold'))
display.grid(row=2, column=0,columnspan=2)

button_reset=Button(master=frame, text='RESET',font=('arial',25,'bold'), width=7,command=lambda:reset())
button_reset.grid(row=1,column=1)

def reset():
    entry.delete(0,END)
    display.delete(0,END)

 
def password_generator(user_input):
    user_input=int(entry.get()) 
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    
    COMBINED_LIST = s1+s2+s3+s4
    rand_digit = random.choice(s3)
    rand_upper = random.choice(s2)
    rand_lower = random.choice(s1)
    rand_symbol = random.choice(s4)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 
    for x in range(user_input - 4): 
        temp_pass = temp_pass + random.choice(COMBINED_LIST) 
        global temp_pass_list
        temp_pass_list = array.array('u', temp_pass) 
        random.shuffle(temp_pass_list) 
    password = "" 
    for x in temp_pass_list: 
        password = password + x 
    display.insert(0,password) 

window.mainloop()
