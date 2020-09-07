"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

"""

# Minha solução 1:
from pygame import mixer
mixer.init()
mixer.music.load('ex021_1.mp3')
mixer.music.play()
input()

# Minha solução 2:
import playsound
playsound.playsound('ex021_2.mp3')
