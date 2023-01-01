### importing necessary libraries ###
from tkinter import *
import random
import pygame

pygame.init()
pygame.mixer.init()  #to initialize the mixer
pygame.mixer.music.load("Funny_music.mp3")  #to load target audio file
pygame.mixer.music.play(-1)  #to play the audio,here (-1) for infinite loop

### initializing window ###
win = Tk() #to create window
win.geometry('750x400') #window's width & height
win.resizable(0, 0) #to fix the size of the window
win.title('ROCK-PAPER-SCISSORS')  #to set the title of the window
win.config(bg = '#856ff8') #to set background color

Label(win, text='Scissors, rock, paper', font='Times 30 bold italic', bg='pink1').pack()
#label() widget - to display text that user can't modify
#win is the name of our window
#text displays on the label as the label
#font is written text form
#pack to organized widget in the form of block


### for USER choice ###

user_take = StringVar() #a string type variable to store user's choice
Label(win, text='Choose any one: scissors, rock, paper', font='arial 20 bold', bg='seashell2').place(x=120, y=70)
Entry(win, font='arial 20', textvariable=user_take, bg ='antiquewhite2').place(x=250, y=130)
#Entry() widget to create an input text field
    #textvariable to retrieve the text to entry widget
    #place() to place the widget at specific position


### for Computer choice ###

comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'scissors'
elif comp_pick == 2:
    comp_pick = 'rock'
else:
    comp_pick = 'paper'

#random.randint() to randomly take any number from the given number(here from 1 to 3)
#if-else conditions works for if comp choose 1 then scissors, else if choose 2 then rock otherwise paper


### funtion to strat the game ###
result = StringVar()
comp = StringVar()
def play():

    user_pick = user_take.get()
    if user_pick == comp_pick:
        result.set('Tie, You both select same')
        comp.set('Computer chose: '+comp_pick)
    elif user_pick == 'scissors' and comp_pick =='rock':
        result.set('YOU LOOSE, computer smashed you with ROCK.')
        comp.set('Computer chose: '+comp_pick)
    elif user_pick == 'scissors' and comp_pick =='paper':
        result.set('YOU WIN, you cut computer into pieces.')
        comp.set('Computer chose: '+comp_pick)
    elif user_pick == 'rock' and comp_pick =='paper':
        result.set('YOU LOOSE, computer wrapped you with PAPER.')
        comp.set('Computer chose: '+comp_pick)
    elif user_pick == 'rock' and comp_pick =='scissors':
        result.set('YOU WIN, you smashed computer with ROCK.')
        comp.set('Computer chose: '+comp_pick)
    elif user_pick == 'paper' and comp_pick =='rock':
        result.set('YOU WIN, you wrapped computer with PAPER.')
        comp.set('Computer chose: '+comp_pick)
    elif user_pick == 'paper' and comp_pick =='scissors':
        result.set('YOU LOOSE, computer cut you into pieces.')
        comp.set('Computer chose: '+comp_pick)
    else:
        result.set('invalid entry:Choose any one -- scissors, rock, paper')
        comp.set('Computer chose: '+comp_pick)



### Function to RESET ###

def Reset():    #this function sets all variable to an empty string
    result.set('')
    user_take.set("")
    comp.set('')



### Function to Exit ###

def Exit(): #this function will quit the game by stopping the mainloop()
    win.destroy()


###### Define Buttons ######
Entry(win, font='arial 15 bold', textvariable=comp, bg='antiquewhite2', width=50,).place(x=95, y=230)
Entry(win, font='arial 15 bold', textvariable=result, bg='antiquewhite2', width=50,).place(x=95, y=270)

Button(win, font='Helvetica 13 bold', text='PLAY', padx=10, bg='seashell4', command=play).place(x=280, y=190)

Button(win, font='arial 13 bold', text='RESET', padx=10, bg='seashell4', command=Reset).place(x=333, y=310)

Button(win, font='Helvetica 13 bold', text='EXIT', padx=10, bg='seashell4', command=Exit).place(x=430, y=190)
#Button() widget to display a button
#command to call a specific function when a button is clicked
win.mainloop()  #to execute the program
