from msvcrt import getch
import pygame

songs = ['song.mp3', 'Arcade.mp3', 'Another_Love.mp3', 'Sweater_Weather.mp3']
pygame.mixer.init()

def play_next_song():
    global songs
    songs = songs[1:] + [songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

def play_last_song():
    global songs
    songs = [songs[-1]] + songs[:-1] # move current song to the back of the list
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

while True:
    key = ord(getch())
    if key == 27: #ESC
        break
    if key == 13: #Enter
        pygame.mixer.music.play()
    if key == 8: #Backspace
        pygame.mixer.music.stop()
    if key == 80: #Down arrow
        play_last_song()
    if key == 72: #Up arrow
        play_next_song()
    


# Keep the program running until the music finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(100)

