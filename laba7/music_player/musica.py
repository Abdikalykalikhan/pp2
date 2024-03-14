from msvcrt import getch
import pygame

_songs = ['song.mp3']
pygame.mixer.init()
'''pygame.mixer.music.load(songs)'''


def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
while True:
    key = ord(getch())
    if key == 27: #ESC
        break
    if key == 13: #Enter
        print('enter!')
    if key == 80: #Down arrow
        pygame.mixer.music.stop()
    if key == 72: #Up arrow
        pygame.mixer.music.play()




# Keep the program running until the music finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

