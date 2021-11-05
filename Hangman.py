def hangman_game():

    import time

    print(" ------------------------------------------------") 
    print("|                                                |")
    print("|                                                |")
    print("|    Welcome to a game of Hangman!!!             |")
    print("|                                                |")
    print("|                                                |")
    print(" ------------------------------------------------")

    # makes everything randomised
    import random

    name = input("What is your name? ")

    print("")
    print("Hello", name, "and I hope you are ready for a game of hangman!!")

    # List of words
    words = ['cheese', 'monke', 'Poopyfarts', 'nuts',
            'cutlery', 'beach', 'examine', 'suffering',
            'sensei', 'logic', 'bubbles', 'cornflour', 
            'determined', 'mitochondria', 'academia', 
            'titans', 'hangman', 'emergency' ]

    # Chooses one random word from the list
    word = random.choice(words)

    # code to find out the number of characters in the word
    x = len(word)

    # Delays the output of the code
    time.sleep(1)

    print("")
    print("")
    print("There are", x, "characters in the word")

    time.sleep(1)

    print("")
    print("Guess the characters: ")

    guesses = ""

    # Number of guesses allowed
    turns = 20

    while turns > 0:

        # Sets a value to count the number of failed guesses
        failed = 0

        # code for the guesses (like if they match with the word or not)
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        
        # Conditons and output for winning the game
        if failed == 0:
            print("")
            print("Congratulations", name, "you are the champion!!")
            print("")
            print("The word was: ", word)
            print("")
            break

        # Code for guessing
        guess = input("guess a character:")
        guesses += guess

        # Code for if the guess is wrong
        if guess not in word:
            turns -= 1 # Subtracts a turn 
            print("")
            print("Not correct, try again.")
            print('')
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("")
                print("Oh no!!", name, "You Lose")
                break
                
hangman_game()
