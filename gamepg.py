#Rock Paper Scissors using tkinter

#Importing modules
from tkinter import *
import random

#Initializing variables for userchoise and list containing elements from file to
#be used between functions
userch = ''
transflist = []

#Resetting scoreboard
file = open('score.txt','w')
file.write('0\nS')
file.close()

def frontf():
    global transflist
    file = open('score.txt','r')
    filelist = file.readlines()
    transflist = filelist
    page = Tk()
    page.title('Rock Papers and Scissors')
    page.geometry('200x100')
    page['background'] = '#34ff00'


    #Functions
    def playbut():
        page.destroy()
        file.close()
        gamepgf()

    #Buttons
    scorenum = filelist[0].strip()
    score = Label(page, text = ('Score: ' + scorenum))


    play = Button(page, command = playbut, text = 'Play', width = 10)

    outcome = filelist[1]
    outtext = ''
    if outcome.strip() == 'S':
        outtext = ''
    else: 
        outtext = outcome

    
    outlabel = Label(page, text = outtext)
    outlabel['background'] = '#34ff00'

    #Geometry
    play.place(relx = .5, rely = .5, anchor = 'center')
    score.place(relx = .75)
    outlabel.place(relx = .5, rely = .90, anchor = 'center')
    mainloop()
    
def gamepgf():
    global transflist,userch
    file = open('score.txt','w')
    

    page2 = Tk()
    page2.title('Rock Papers and Scissors')
    page2['background'] = '#34ff00'

    #Functions
    
    def rockf():
        global userch
        yourchoice['text'] = 'Rock'
        userch = 'Rock'
    def paperf():
        global userch
        yourchoice['text'] = 'Paper'
        userch = 'Paper'
    def scissorsf():
        global userch
        yourchoice['text'] = 'Scissors'
        userch = 'Scissors'
    def run():
        global userch
        
        compch = random.choice(['Rock','Paper','Scissors'])
        
        if compch == userch:
            file.write(transflist[0] + f'It is a draw. Computer chose {compch}.')
        elif ((userch == 'Rock' and compch == 'Paper') == True) or ((userch == 'Scissors' and compch == 'Rock') == True) or ((userch == 'Paper' and compch == 'Scissors') == True):
            file.write(transflist[0] + f'You lose. Computer chose {compch}.')
        elif userch == '':
            file.write(transflist[0] + 'User did not make a choice.')
        else:
            newscore = str(int(transflist[0].strip()) + 1)
            file.write(newscore + '\n' + f'You win! Computer chose {compch}.')
        page2.destroy()
        file.close()
        frontf()
        

    #Variables
    userch = ''


    #Widgets
    scorenum = transflist[0].strip()
    score = Label(page2, text = ('Score: ' + scorenum))
    

    
    chooselabel = Label(page2, text = 'Choose: ')
    chooselabel['background'] = '#34ff00'

    rockimg = PhotoImage(file = 'rock.png')    
    rock = Button(page2,  command = rockf, image = rockimg, width = 175, height = 120)
    paperimg = PhotoImage(file = 'paper.png')
    paper = Button(page2, image = paperimg, command = paperf, width = 175, height = 120)
    scissorsimg = PhotoImage(file = 'scissors.png')
    scissors = Button(page2, image = scissorsimg, command = scissorsf, width = 175, height = 120)

    chosen = Label(page2, text = 'Chosen: ')
    chosen['background'] = '#34ff00'
    yourchoice = Label(page2, text = '')
    yourchoice['background'] = '#34ff00'

    continuebtn = Button(page2, text = 'Continue', width = 10, command = run)

 
    #Geometry Managers
    score.grid(row = 0, column = 2)

    
    chooselabel.grid(row = 1, column = 0)

    rock.grid(row = 2, column = 0, padx = 5)
    paper.grid(row = 2, column = 1, padx = 5)
    scissors.grid(row = 2, column = 2, padx = 5)

    chosen.grid(row = 3, column = 0)
    yourchoice.grid(row = 3, column = 1)

    continuebtn.grid(row = 4, column = 1)
    mainloop()
frontf()

