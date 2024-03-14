import pygame

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == SONG_END:
            print("the song ended!")