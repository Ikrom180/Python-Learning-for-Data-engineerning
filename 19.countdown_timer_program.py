import time as t

# t.sleep(3)
#
# print("That is time")

my_time = int(input("Enter the time in a second: "))

for x in range(my_time, 0 , -1):
    hour = int(x / 3600)
    minutes = int(x/60) % 60
    seconds = x % 60
    print(f'{hour:02}:{minutes:02}:{seconds:02} ')
    t.sleep(1)

print('Time`s is up')

