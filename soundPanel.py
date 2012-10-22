import tkinter
import pygame.mixer

class SoundPanel(tkinter.Frame):

	#Initializer
	def __init__(self, app, mixer, soundFile):
		#initialize Frame
		tkinter.Frame.__init__(self, app)

		#set song
		self.song = mixer.Sound(soundFile)

		#set Checkbutton portion
		self.toggleVal = tkinter.IntVar()
		toggle = tkinter.Checkbutton(self, text = "Play/Stop: %s" % soundFile, 
									variable = self.toggleVal, command = self.toggleSong)
		toggle.pack(side = 'left')

		#set Slider portion
		self.volLvl = tkinter.DoubleVar()
		volSlider = tkinter.Scale(self, from_ = 0.0, to = 1.0, resolution = 0.05, orient = 'horizontal', 
									label = "Volume", variable = self.volLvl, command = self.volCntrl) 
		volSlider.pack(side = 'right')

	#Checkbutton behavior
	def toggleSong(self):
		if self.toggleVal.get() == 1:
			self.song.play(loops = -1)
		else:
			self.song.stop()

	#Slider behavior
	def volCntrl(self, v):
		self.song.set_volume(self.volLvl.get())

	def stopTrack(self):
		self.song.stop()