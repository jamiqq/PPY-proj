import pygame

# Initialize the pygame mixer for audio playback
pygame.mixer.init()

# Load and play background music from the specified file path.
def play_background_music(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

# Stop the currently playing background music.
def stop_background_music():
    pygame.mixer.music.stop()

# Play a short sound effect from the specified file path.
def play_sound_effect(path):
    sound = pygame.mixer.Sound(path)
    sound.play()
