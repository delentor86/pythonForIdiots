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
    print(timerNumber) 
    

randomNumber()


