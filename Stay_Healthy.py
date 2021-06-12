"""It is project  for the people who use Pc continuously so this program will remind them to drink water in every 45 min
 ,to do eye exercise in every 30 min, and to do exercise in 55 minutes.
  you can also change time just by changing time digits after mention "time" comment """
import pygame
import datetime
import time


def musicloop(filename, stopper):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while True:
        input_by_the_user = input()
        if input_by_the_user == stopper:
            pygame.mixer.music.stop()
            break


def log_now(msg):
    with open("health_logs.txt", "a") as f:
        f.write(f"{msg} {datetime.datetime.now()}\n")


if __name__ == '__main__':

    init_water = time.time()
    init_eye = time.time()
    init_exercise = time.time()
    # time
    watersecs = 45 * 60
    eyesecs = 30 * 60
    exercisesecs = 55 * 60

    while True:
        if time.time()-init_water > watersecs:
            print("Its time to drank some water!!press 'drank' if you have")
            musicloop('water.mp3', 'drank')
            init_water = time.time()
            log_now("water has been drank at ")

        if time.time() - init_eye > eyesecs:
            print("Your eyes need some Exercise!!press 'done' if you have")
            musicloop('eyes.mp3', 'done')
            init_eye = time.time()
            log_now("Eye exercise has been done at ")

        if time.time() - init_exercise > exercisesecs:
            print("Its time to do some Exercise!!press 'done' if you have")
            musicloop('physical.mp3', 'done')
            init_exercise = time.time()
            log_now("Exercise has been done at ")
