import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
pygame.event.wait()
print('\033[1;95m-=-' * 7)
print('\033[97m    La \033[93mCatholique')
print('\033[95m-=-' * 7)
a = ''
while a == '':
    a = str(input('')).upper()
    if a == 'PAUSE':
        pygame.mixer.music.pause()
    if a == 'UNPAUSE':
        pygame.mixer.music.unpause()
    if a == 'RESTART':
        pygame.mixer.music.rewind()
    if a == 'STOP':
        pygame.mixer.music.stop()
    if a == 'START':
        pygame.mixer.music.play()
    if a == 'EXIT':
        exit()
    a = ''
