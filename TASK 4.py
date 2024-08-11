#importing the basic library that we will use for the development of this project
from tkinter import *
from PIL import Image, ImageTk
import random

#these are some of the variables that we will use in rock paper and scissor game
userscore = 0
pcscore = 0

#these are various functions that will help us to handle all the events that will take place in this project
#we also used the config() function to configure the various widgets like its color, size etc
def enter(event):
    rock.config(bg='black', fg='white')

def enter1(event):
    paper.config(bg='black', fg='white')

def enter2(event):
    scissor.config(bg='black', fg='white')

def leave(event):
    rock.config(bg='white', fg='black')

def leave1(event):
    paper.config(bg='white', fg='black')

def leave2(event):
    scissor.config(bg='white', fg='black')

def entergame(event):
    maingame()

#Maingame Function will bring a new window of GUI and will provide a platform to play rock paper and scissor Game
def maingame():
    global userscore, pcscore
    global nameinp
    global rock, paper, scissor

    root.geometry('650x750')
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()

    # Display scores
    L2 = Label(text=f"{nameinp.get()} Score: {userscore}", bg='#4834DF', fg='#ffffff', borderwidth=5, relief=RAISED, font='Rockwell 13 bold', padx=4, pady=2)
    L2.grid(row=6, column=0, pady=15)
    L3 = Label(text=f"PC Score: {pcscore}", bg='#4834DF', fg='white', borderwidth=5, relief=RAISED, font='Rockwell 13 bold', padx=4, pady=2)
    L3.grid(row=7, column=0, pady=15)

    def click(event):
        global userscore, pcscore
        global L1     
        global pcchose  
        L1.grid_forget()
        pcchose.destroy()

        val = event.widget.cget('text')

        x = random.randint(0, 2)
        l1 = ['Rock', 'Paper', 'Scissor']
        pc_opt = l1[x]

        pcchose = Label(text=f'PC Opted: {pc_opt}', font='lucida 15 bold', bg='black', fg='red')
        pcchose.grid(row=6, column=1, pady=15)

        if val == 'Rock' and pc_opt == 'Paper':
            L1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            pcscore += 1
        elif val == 'Rock' and pc_opt == 'Scissor':
            L1 = Label(text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=6, column=1, pady=15)
            userscore += 1
        elif val == 'Paper' and pc_opt == 'Scissor':
            L1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            pcscore += 1
        elif val == 'Paper' and pc_opt == 'Rock':
            L1 = Label(text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            userscore += 1
        elif val == 'Scissor' and pc_opt == 'Rock':
            L1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            pcscore += 1
        elif val == 'Scissor' and pc_opt == 'Paper':
            L1 = Label(text=f'{nameinp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)
            userscore += 1
        elif val == pc_opt:
            L1 = Label(text=f"It's A Tie", font='lucida 15 bold', bg='black', fg='gold')
            L1.grid(row=7, column=1, pady=15)

        maingame()

    # Overall Layout of RPS Game
    head = Label(text='Rock Paper Scissor', font='arial 35 bold', bg='black', fg='white')
    head.grid(columnspan=2, row=0, ipadx=70, padx=33, pady=10)
    playerone = Label(text=f'Player 1 : {nameinp.get()}', font='lucida 16')
    playerone.grid(row=2, column=0)
    playertwo = Label(text=f'Player 2 : Computer', font='lucida 16')
    playertwo.grid(row=2, column=1)

    rock = Button(text='Rock', font='comicsansms 14 bold', height=1, width=7)
    rock.grid(row=3, column=0, pady=15)
    rock.bind('<Enter>', enter)
    rock.bind('<Leave>', leave)
    rock.bind('<Button-1>', click)
    paper = Button(text='Paper', font='comicsansms 14 bold', height=1, width=7)
    paper.grid(row=4, column=0)
    paper.bind('<Enter>', enter1)
    paper.bind('<Leave>', leave1)
    paper.bind('<Button-1>', click)
    scissor = Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7)
    scissor.grid(row=5, column=0, pady=15)
    scissor.bind('<Enter>', enter2)
    scissor.bind('<Leave>', leave2)
    scissor.bind('<Button-1>', click)

    rock1 = Button(text='Rock', font='comicsansms 14 bold', height=1, width=7)
    rock1.grid(row=3, column=1, pady=15)
    paper1 = Button(text='Paper', font='comicsansms 14 bold', height=1, width=7)
    paper1.grid(row=4, column=1)
    scissor1 = Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7)
    scissor1.grid(row=5, column=1, pady=15)

    btnclose = Button(text='Close Game', command=root.destroy, bg='green', font='arial 10 bold')
    btnclose.place(x=300, y=410)

# now the actual programming of the GUI starts
root = Tk()
root.title('Rock Paper Scissor')

# Comment out or remove the following line if you're not using a custom icon
# root.wm_iconbitmap("play.ico")

root.geometry('650x750')
root.maxsize(650, 750)
root.minsize(650, 450)

# Defining some widgets to use them in different functions
rock = Button()
paper = Button()
scissor = Button()

L1 = Label()
pcchose = Label()

# Initial frame with image
f1 = Frame(root)
img = Image.open('symbols.png')
img = img.resize((650, 450), Image.LANCZOS)  # Use Image.LANCZOS for resampling
pic = ImageTk.PhotoImage(img)
Lab = Label(f1, image=pic)
Lab.pack()
f1.pack()

name = Label(root, text='Enter Your Name :', font='arial 15 bold')
name.place(x=262, y=250)

nameinp = StringVar()
inpname = Entry(root, textvar=nameinp, font='arial 10 bold')
inpname.bind('<Return>', entergame)
inpname.place(x=275, y=290)  # Make sure to close the parentheses here

sub = Button(root, text='Submit', font='arial 10 bold', command=entergame)
sub.place(x=275, y=330)

root.mainloop()
