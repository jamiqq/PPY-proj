# sound_manager.py
import pygame

pygame.mixer.init()

def play_background_music(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

def stop_background_music():
    pygame.mixer.music.stop()

def play_sound_effect(path):
    sound = pygame.mixer.Sound(path)
    sound.play()
