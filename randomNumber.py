import time
import random


def rand_numbers():
    numOne = random.randint(30, 44)
    numTwo = random.randint(30, 44)
    numThree = random.randint(30, 44)

    if numOne > numTwo and numOne > numThree:
        rando_Numbo = numOne
    elif numTwo > numOne and numTwo > numThree:
        rando_Numbo = numTwo
    else:
        rando_Numbo = numThree
    return (rando_Numbo)


# countdown function
def countdown(t):
    # while loop for countdown
    while t:
        mins, secs = divmod(t, 60)
        t = '{:02d}:{:02d}'.format(mins, secs)
        print(t)
        time.sleep(1)


# function call and assigned returned number to t
t = rand_numbers() * 60

# function call
countdown(int(t))
