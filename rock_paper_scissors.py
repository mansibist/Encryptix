import random
from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("***********Rock Paper Scissors***********")
root.configure(background="lightblue")
frame =Frame(master=root, bg="purple", padx=10)
frame.pack()
w=Label(master=frame,text='!!!WELCOME!!!',font=('arial',35,'bold'),bg="lightblue",fg="black").grid(row=0,column=2)

image_rock1=ImageTk.PhotoImage(Image.open("D:\\rock.png"))
image_rock2=ImageTk.PhotoImage(Image.open("D:\\rock.png"))
image_paper1=ImageTk.PhotoImage(Image.open("D:\\paper.png"))
image_paper2=ImageTk.PhotoImage(Image.open("D:\\paper.png"))
image_scissors1=ImageTk.PhotoImage(Image.open("D:\\scissors.png"))
image_scissors2=ImageTk.PhotoImage(Image.open("D:\\scissors.png"))
image_user=ImageTk.PhotoImage(Image.open("D:\\person_icon.png"))
image_computer=ImageTk.PhotoImage(Image.open("D:\\computer-icon.png"))
image_rock=ImageTk.PhotoImage(Image.open("D:\\rock1.png"))
image_paper=ImageTk.PhotoImage(Image.open("D:\\paper1.png"))
image_scissors=ImageTk.PhotoImage(Image.open("D:\\scissors1.png"))

img_Computer=Label(master=frame,image=image_computer)
img_Computer.grid(row=2,column=0)
img_Player=Label(master=frame,image=image_user)
img_Player.grid(row=2,column=4)

score_comp=Label(master=frame,text=0,font=('arial',60,"bold"),bg="orange",fg="white")
score_comp.grid(row=2,column=1)
score_player=Label(master=frame,text=0,font=('arial',60,"bold"),bg="orange",fg="white")
score_player.grid(row=2,column=3)

com_text=Label(master=frame,text="COMPUTER",font=('arial',40,"bold"),bg='pink',fg='black')
com_text.grid(row=1,column=0,columnspan=2)
pla_text=Label(master=frame,text="PLAYER",font=('arial',40,"bold"),bg='pink',fg='black')
pla_text.grid(row=1,column=3,columnspan=2)

def update_msg(a):
    result['text']=a

def update_compScore():
    final=int(score_comp['text'])
    final+=1
    score_comp["text"]=str(final)

def update_playScore():
    final=int(score_player['text'])
    final+=1
    score_player["text"]=str(final)

def Winner_checking(p,c):
    if p==c:
         update_msg("IT'S A TIE!!!")
    elif p=="rock":
        if c=="paper":
            update_msg("COMPUTER WINS!!!")
            update_compScore()
        else:
            update_msg("PLAYER WINS!!!")
            update_playScore()
    elif p=="paper":
        if c=="scissors":
            update_msg("COMPUTER WINS!!!")
            update_compScore()
        else:
            update_msg("PLAYER WINS!!!")
            update_playScore()
    elif p=="scissors":
        if c=="rock":
            update_msg("COMPUTER WINS!!!")
            update_compScore()
        else:
            update_msg("PLAYER WINS!!!")
            update_playScore()
    else:
        pass

option=["rock","paper","scissors"]

def option_update(b):
    computer_choice=option[random.randint(0,2)]
    if computer_choice=="rock":
        img_Computer.configure(image=image_rock2)
    elif computer_choice=="paper":
        img_Computer.configure(image=image_paper2)
    else:
        img_Computer.configure(image=image_scissors2)

    if b=="rock":
        img_Player.configure(image=image_rock1)
    elif b=="paper":
        img_Player.configure(image=image_paper1)
    else:
        img_Player.configure(image=image_scissors1)

    Winner_checking(b,computer_choice)

result=Label(master=frame,text='',font=("arial",40,'bold'),bg='yellow',fg='black')
result.grid(row=5,column=2)

img_rock=Label(master=frame,image=image_rock)
img_rock.grid(row=3,column=1)
img_paper=Label(master=frame,image=image_paper)
img_paper.grid(row=3,column=2)
img_scissors=Label(master=frame,image=image_scissors)
img_scissors.grid(row=3,column=3)
button_rock=Button(master=frame,width=30,height=3,text='ROCK',font=('arial',10,'bold'),bg='green',fg='black',command=lambda:option_update("rock")).grid(row=4,column=1)
button_paper=Button(master=frame,width=30,height=3,text='PAPER',font=('arial',10,'bold'),bg='green',fg='black',command=lambda:option_update("paper")).grid(row=4,column=2)
button_scissors=Button(master=frame,width=30,height=3,text='SCISSORS',font=('arial',10,'bold'),bg='green',fg='black',command=lambda:option_update("scissors")).grid(row=4,column=3)

root.mainloop()






