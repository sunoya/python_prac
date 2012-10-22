import tkinter
import pygame

def cPress():
	applause.play()
	numCorrect.set(numCorrect.get()+1)

def wPress():
	buzz.play()
	numWrong.set(numWrong.get()+1)

#initialize sounds
sounds = pygame.mixer
sounds.init()
buzz = sounds.Sound("buzz.wav")
applause = sounds.Sound("applause.wav")

#initialize window
app = tkinter.Tk()
app.geometry('400x200+300+200')
app.title("Super Awesome Quiz")

#initialize count variables
numCorrect = tkinter.IntVar()
numCorrect.set(0)
numWrong = tkinter.IntVar()
numWrong.set(0)

#Simple text in a window
label = tkinter.Label(app, text = "How did the contestant answer?")
label.pack(side = 'top', pady = 20)	

#Adding buttons
b1 = tkinter.Button(app, text = "Correct!", width = 10, height = 2, command = cPress)
b2 = tkinter.Button(app, text = "Wrong!", width = 10, height = 2, command = wPress) 
#state='disabled', relief = 'sunken'

cCount = tkinter.Label(app, textvariable = numCorrect)
cCount.pack(side = 'left', padx = 8)
wCount = tkinter.Label(app, textvariable = numWrong)
wCount.pack(side = 'right', padx = 8)

#place buttons into window
b1.pack(side = 'left', padx = 20)
b2.pack(side = 'right', padx = 20)
app.mainloop()

