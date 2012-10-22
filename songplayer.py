import tkinter
import pygame.mixer


"""
def playSong():
	song.play(loops = -1)

def stopSong():
	song.stop()
"""

#Window close function
def closeWindow():
	song.stop()
	window.destroy()

#On/Off function
def toggleSong():
	if toggleVal.get() == 1:
		song.play(loops = -1)
	else:
		song.stop()

#Volume Control Function
def volCntrl(v):
	song.set_volume(volLvl.get())


musicFile = "50459_M_RED_Nephlimizer.wav"

#initialize sound
music = pygame.mixer
music.init()
song = music.Sound(musicFile)

#create GUI
window = tkinter.Tk()
window.title("Music Player")

#On/Off Toggle
toggleVal = tkinter.IntVar()
toggle = tkinter.Checkbutton(window, text = "Play/Stop: %s" % musicFile, 
								variable = toggleVal, command = toggleSong)
toggle.pack(side = 'left')

#Volume Slider
volLvl = tkinter.DoubleVar()
volSlider = tkinter.Scale(window, from_ = 0.0, to = 1.0, resolution = 0.05, command = volCntrl,
							label = "Volume", variable = volLvl, orient = 'horizontal') 
volSlider.pack(side = 'right')

"""
stop = tkinter.Button(window, text = "Stop", width = '10', height = '2', command = stopSong)
stop.pack(side = 'right', padx = 20)

start = tkinter.Button(window, text = "Play", width = '10', height = '2', command = playSong)
start.pack(side = 'left', padx = 20)
"""

#Window closed functionality
window.protocol("WM_DELETE_WINDOW", closeWindow)

window.mainloop()

