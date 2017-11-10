# create a function to get the number of cows and bulls
def cows_and_bulls(guess, answer):
    """(int, int) -> (int, int)
    
    Returns a tupple of two integers. The first integer is the number of digits 
    guess has in common with answer and are in the same place. The second integer 
    is the number of digits guess has in common with answer but are not in the same place.
    
    Pre-condition: len(str(guess)) == len(str(answer))
    
    >>>cows_and_bulls(3452,3092)
    [2,0]
    >>>cows_and_bulls(1024, 3092)
    [1,1]
    """
    #initialize cows and bulls
    cows = 0
    bulls = 0
    
    #convert guess and answer to str for easy comparison
    guess = str(guess)
    answer = str(answer)
    
    for i in range(len(guess)):
        if answer[i] == guess[i]:
            cows = cows+1
        elif answer[i] in guess:
            bulls = bulls+1
            
    return (cows, bulls)

def main():
    try:
        # get a random 4 digit number
        import random
        answer = random.randint(1000,9999)
                
        print("Welcome to the cows and bulls game!!\n\n"
              "For each guess you will get the no. of cows(digit that the \n"
              "user guessed correctly in the correct place) and bulls (digit \n"
              "that the user guessed correctly but in the wrong place.\n"
              "The game will continue untill the correct number is guessed.\n\n"
              "If you want to quit anytime, enter exit.")

        # initialize counter
        counter = 0
        invalid_input = True
        while invalid_input:
            usr_input = input("Please enter a 4 digit number: ")
            
            # if user enters exit, stop the game
            if usr_input.lower() == 'exit':
                print("You have quit the game. So far you made %s guess." %counter)
                invalid_input = False
                
            # if the entered input is valid, call the function cows_and_bulls and increment the counter
            elif usr_input.isdigit() and len(usr_input) == 4:
                guess = int(usr_input)
                
                # activate below code to debug
                # print(guess, answer)
                
                print("Cows: %s, Bulls: %s" % (cows_and_bulls(guess,answer)))
                counter = counter+1
                
                # if guess is right, end the game.
                if guess == answer:
                    print("Congratulations!! Your guess is write. You took %s attemps for this" %counter)
                    invalid_input = False
                    
            # if the input is not valid show appropriate message.
            else:
                print("Incorrect input. Please try again.")
    except:
        print("Something went wrong...")
    input("press enter to exit....")

if __name__ == '__main__':
    main()
