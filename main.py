import zipfile, fnmatch, os
import pygame
import glob


def playSound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


rootPath = r'/users/russelcorbo/downloads'
pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))

print(glob.glob('./*'))
os.chdir('/users/russelcorbo/Desktop/')

pygame.init()
playSound('Water-Drop.wav')
