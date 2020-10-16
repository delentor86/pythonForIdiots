#random time generator that favors higher number
def randomNumber():

    import random
    numberOne = random.randint(30,44)
    numberTwo = random.randint(30,44)
    
	#if statements to save higher of two die rolls
    if numberOne >= numberTwo:
        timerNumber = numberOne
    else: 
        timerNumber = numberTwo
    print(timerNumber) 
	
#function call for randomNumber
randomNumber()