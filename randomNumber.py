#This original terrible code written by delentor86@gmail.com 

#creating timer object
class Alarm:
	def __init__(self, timers):



#random time generator that favors higher number
def randomNumber():

    import random
	#first variable
    numberOne = random.randint(30,44)
	#second variable
    numberTwo = random.randint(30,44)
    #third roll
    numberThree = random.randint(30,44)
    
	#compare the variables and keep the highest
    if numberOne > numberTwo and numberOne > numberThree:
        timerNumber = numberOne
        
    elif numberTwo > numberOne and numberTwo > numberThree:
        timerNumber = numberTwo
        
    else: 
        timerNumber = numberThree
        
    return(timerNumber)
	
    #function call for randomNumber
