#getting variable for random minute value for timer
def randomNumber():
    
    import random
    
    rollOne = random.randint(30,44)
    rollTwo = random.randint(30,44)
    rollThree = random.randint(30,44)
    
    if rollOne > rollTwo and rollOne > rollThree: 
        timerNumber = rollOne
    elif rollTwo > rollThree and rollTwo > rollOne: 
        timerNumber = rollTwo
    else:
        timerNumber = rollThree
    return(timerNumber)

#main function will call randomNumber function and display results
def main():
    timer = randomNumber()
    print(timer)
main()
