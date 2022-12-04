# timeryoutube.py
# author: bro code
# date: 1.12.2022

# count up
'''
import time

running = True
seconds = 0
end = 10

while(running):
    print(seconds)
    time.sleep(1)
    seconds += 1
    if(seconds >= end):
        running = False
        print(seconds)
print("Done!")
'''

# count down
import time

running = True
seconds = 10
end = 0

while(running):
    print(seconds)
    time.sleep(1)
    seconds -= 1
    if(seconds >= end):
        running = False
        print(seconds)
print("Happy New Year!")
