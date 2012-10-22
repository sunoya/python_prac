import pygame.mixer


def isBusy(channel):
	while channel.get_busy():
		pass

sounds = pygame.mixer
sounds.init()
correctSound = sounds.Sound("heartbeat.wav")
wrongSound = sounds.Sound("buzz.wav")

hostResp = 1
numCorrect = 0
numAsked = 0
numWrong = 0

while hostResp != 0:
	hostIn = input("Press 1 for a correct answer and 2 for a wrong answer. 0 to quit: ")
	hostResp = int(hostIn)
	if hostResp == 1:
		numCorrect += 1
		numAsked += 1
		isBusy(correctSound.play())
	if hostResp == 2:
		numWrong += 1
		numAsked += 1
		isBusy(wrongSound.play())

print("Number correct: " + str(numCorrect))
print("Number wrong: " + str(numWrong))
print("Questions asked: " + str(numAsked))


