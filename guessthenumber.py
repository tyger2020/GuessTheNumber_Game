import simplegui
import random


secret_number = 0 # the computer's number
max_num = 0 # the number of guesses, depending on the range



# helper function to start and restart the game
def range100():
    # button that changes the range to [0,100) and starts a new game
    print "Enter a number between 0 and 100."
    global secret_number
    secret_number = random.randint(0, 100)
    global max_num
    max_num = 7
    #make sure the button does something by printing secret_number
    
    
def new_game():
    # initialize global variables used in your code here
    range100()
    
    #your number guess
    u_guess = 0
    

    




    
     
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "Enter a number between 0 and 1000."
    global secret_number
    secret_number = random.randint(0, 1000)
    global num_guess
    num_guess = 0
    global max_num
    max_num = 10
    #Test if the button response works, comment out when program is running
    #print max_num
    #print secret_number
    
        

    
def input_guess(guess):
    
    
    #takes a user input
    u_guess = int(guess)
    print "Guess was", u_guess
    
    
        
    
    global secret_number
    global max_num
    
    if (u_guess < secret_number):
        
        max_num = max_num - 1
        if (max_num == 0):
            print "Number of guesses exhausted."
            print "The number was", secret_number
            print "Play again."
            print " "
            print " "
            new_game()
        else:
            
            print "Number of remaining guesses is", max_num
            print "Higher!"
        
        
            print " "
    elif (u_guess > secret_number):
        
        #decrements number of guesses left, tests if num_guesses has run out
        max_num = max_num - 1
        if (max_num == 0):
            print "Number of guesses exhausted. Play again."
            print "The number was", secret_number
            print "Play again."
            print " "
            print " "
            new_game()
            
        else:
            
            print "Number of remaining guesses is", max_num
            print "Lower!"
        
        
            print " "
        
        
          
        
    else:
        print "Correct! Play again."
        print " "
        print " "
        new_game()
        
    
    
    

    
# create frame
f = simplegui.create_frame("Guess the number", 300, 300)
f.add_button("Range 0-100", range100, 100)
f.add_button("Range 0-1000", range1000, 100)
f.add_input("Enter", input_guess, 200)


# register event handlers for control elements and start frame


# call new_game
new_game()
