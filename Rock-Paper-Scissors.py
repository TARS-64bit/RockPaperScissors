
from tkinter import *
import random

root = Tk()
root.geometry('400x500')
root.resizable(0,0)
root.title('Python - Rock, Paper, Scissors')
root.config(bg ='#000')

Label(root, text = 'Rock, Paper ,Scissors', font='arial 20 bold', foreground = "#fff", bg = '#000').pack()

user_inp = StringVar()
Label(root, text = 'Choose one: Rock, Paper or Scissors' ,foreground = "#ddd", bg = '#000', font='arial 15 bold').place(x = 15,y=70)
Entry(root, font = 'arial 15', textvariable = user_inp, border= "0", bg = '#666', foreground="#fff").place(x=90 , y = 130)

    
Result = StringVar()

def play():
    comp_pick = random.randint(1,3)
    if comp_pick == 1:
        comp_pick = 'rock'
    elif comp_pick ==2:
        comp_pick = 'paper'
    else:
        comp_pick = 'scissors'

    user_pick = user_inp.get().lower()
    if user_pick == comp_pick:
        Result.set('Tie, Computer and you both selected ' + str(user_pick).capitalize())
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You lost, Computer selected paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You won, Computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You loose, Computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You won, Computer selected rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You loose, Computer selected rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You won, Computer selected paper')
    else:
        Result.set('invalid: choose any one -- Rock, Paper, Scissors')
    
def reset():
    Result.set("") 
    user_inp.set("")

def exit():
    root.destroy()

Entry(root, font = 'arial 10', textvariable = Result,  border= "0", bg = '#666', foreground="#fff",width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13', border="0", cursor="circle",  text = 'PLAY'  ,padx =5, bg = '#444', foreground="#fff",command = play).place(x=170,y=190)

Button(root, font = 'arial 13', border="0", cursor="circle", text = 'RESET'  ,padx =5, bg = '#444', foreground="#fff",command = reset).place(x=90,y=310)

Button(root, font = 'arial 13', border="0", cursor="circle", text = 'EXIT'  ,padx =5, bg = '#444', foreground="#fff",command = exit).place(x=250,y=310)

root.mainloop()
