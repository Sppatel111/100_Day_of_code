# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds
# or at a particular time.
import time
import pygame


def set_alarm(seconds=None, alarm_time=None):
    if seconds is not None:
        print(f"Alarm set for {seconds} seconds.")
        time.sleep(seconds)
        print("Time's up!")
        play_alarm_sound()
    elif alarm_time is not None:
        print(f"Alarm set for {alarm_time}.")
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                print("Time's up!")
                play_alarm_sound()
                break
            time.sleep(30)
    else:
        print("Please set either seconds or alarm time.")


def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('alarm_sound.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


set_alarm(seconds=3, alarm_time="12:53")
