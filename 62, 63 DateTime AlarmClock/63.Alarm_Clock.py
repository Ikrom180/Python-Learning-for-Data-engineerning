#Python Alarm clock
import time
import datetime
import pygame

def set_alarm(alarm_time1):
    print("alarm time:", alarm_time1)
    sound_file = "Feel-Good(chosic.com).mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time1:
            print("Wake up!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(10)


            is_running = False

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time: (HH:MM:SS): ")
    set_alarm(alarm_time)