#Rock Paper Scissors using tkinter

#Importing modules
from tkinter import *
import random

#Initializing variables for userchoise and list containing elements from file to
#be used between functions
userch = ''
scorenum = 0
count = 0
initcount = 0

#Resetting scoreboard
file = open('score.txt','w')
file.write(' ')
file.close()

def frontf():
    global scorenum, count, initcount
    file = open('score.txt','r')
    filelist = file.readlines()
    file.close()

    file = open('gamecount.txt','w')
    file.write('Enter the no. of games you wish to play.')
    file.close()
    
    page = Tk()
    page.title('Rock Papers and Scissors')
    page.geometry('450x375')
    page['background'] = '#34ff00'


    #Functions
    def playbut():
        global count, initcount
        count = gamecnt.get()
        initcount = count
        if count.isdigit() == True:
            page.destroy()
            gamepgf()
        else:
            outlabel['text'] = 'Please enter a valid value.'
            

    #Buttons
    score = Label(page, text = ('Score: ' + str(scorenum)))

    mainimg = PhotoImage(file = 'main.png')
    rpsimg = Label(page, image = mainimg)

    gamecnt = Entry(page, width = 50)
    file = open('gamecount.txt','r')
    gamecnt.insert(0, file.readlines()[0])
    file.close()
    
    play = Button(page, command = playbut, text = 'Play', width = 10)

    outlabel = Label(page, text = filelist[0])
    outlabel['background'] = '#34ff00'

    #Geometry
    score.place(relx = .90, rely = .05, anchor = 'center')
    rpsimg.place(relx = .5, rely = .40, anchor = 'center')
    gamecnt.place(relx = .5, rely = .78, anchor = 'center')
    outlabel.place(relx = .5, rely = .85, anchor = 'center')
    play.place(relx = .5, rely = .93, anchor = 'center')
    mainloop()
    
def gamepgf():
    global scorenum, userch, count
    scorenum = 0
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
      global scorenum, userch, count
      if int(count) != 0:
        compch = random.choice(['Rock','Paper','Scissors'])
        outcome['text'] = 'Result:'
        if compch == userch:
            result['text'] = f'It is a draw. Computer chose {compch}.'
            scorenum += .5
            score['text'] = ('Score: ' + str(scorenum))
        elif ((userch == 'Rock' and compch == 'Paper') == True) or ((userch == 'Scissors' and compch == 'Rock') == True) or ((userch == 'Paper' and compch == 'Scissors') == True):
            result['text'] = f'You lose. Computer chose {compch}.'
        elif userch == '':
            result['text'] = 'User did not make a choice.'
            
        else:
            result['text'] = f'You win! Computer chose {compch}.'
            scorenum += 1
            score['text'] = ('Score: ' + str(scorenum))
        count = str(int(count)- 1)
      else:
          page2.destroy()
          file = open('score.txt','w')
          file.write(f'Your score: ({scorenum}/{initcount})')
          file.close()
          frontf()
          
        
        

    #Variables
    userch = ''


    #Widgets
    score = Label(page2, text = ('Score: ' + str(scorenum)))
    

    
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

    outcome = Label(page2, text = '')
    outcome['background'] = '#34ff00'
    result = Label(page2, text = '')
    result['background'] = '#34ff00'
    
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

    outcome.grid(row = 5, column = 0)
    result.grid(row = 5, column = 1)

    
    mainloop()
frontf()

