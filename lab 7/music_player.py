import pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))

background = pygame.image.load("/Users/uldanakonyratbaeva/Desktop/lab 7/pink spotify.jpg")
background = pygame.transform.scale(background, (300, 300))

songs = ["/Users/uldanakonyratbaeva/Desktop/lab 7/Lana Del Rey - Diet Mountain Dew.mp3", 
         "/Users/uldanakonyratbaeva/Desktop/lab 7/Lana Del Rey - Doin' Time.mp3", 
         "/Users/uldanakonyratbaeva/Desktop/lab 7/Lana Del Rey - West Coast.mp3"]

current_song = 0

pygame.mixer.init()

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

music = True

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music:
                    pygame.mixer.music.pause()
                    music = False
                else:
                    pygame.mixer.music.unpause()
                    music = True

            elif event.key == pygame.K_RIGHT:
                current_song+=1
                if current_song>=len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                current_song-=1
                if current_song<0:
                    current_song = len(songs) - 1
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip()