# Multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Goof for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)


import threading
import time

def walk_dog(first, second):
    time.sleep(8)
    print(f"You finish walking the dog {first} and {second}")

def take_out_trash(name):
    time.sleep(2)
    print(f"You take out the trash {name}")

def get_email():
    time.sleep(4)
    print("You get the email")

#If i write like that it will take 14 sek
# walk_dog()
# take_out_trash()
# get_email()

# if i write it with thread it will take 8 sek bc it will run concurrently
chore1 = threading.Thread(target=walk_dog, args=('Scooby','Doo'))
chore1.start()

chore2 = threading.Thread(target=take_out_trash, args=('trash_name',)) #-> if only one arg given we have to write comme
chore2.start()

chore3 = threading.Thread(target=get_email)
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("All chores are completed")