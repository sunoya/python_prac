import soundPanel
import tkinter
import pygame.mixer
import os

#Window close function
def closeWindow():
	for tracks in trackArray:
		tracks.stopTrack()
	window.destroy()

music = pygame.mixer
music.init()

window = tkinter.Tk()
window.title("Music Player")

dirList = os.listdir(".")

trackArray = []

for files in dirList:
	if files.endswith(".wav"):
		panel = soundPanel.SoundPanel(window, music, files)
		trackArray.append(panel)
		panel.pack()

window.protocol("WM_DELETE_WINDOW", closeWindow)

window.mainloop()