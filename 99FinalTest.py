# Assigns a function to the whole menu
def my_menu():
    import os # clear statement
    os.system('cls')

    print(" ------------------------------------------------") 
    print("|                                                |")
    print("|    99FinalTest                                 |")
    print("|    Name : Nikhita Arora                        |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print("")

    # List
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    answer = input("Enter an option ")

    # if...else statements for the output of each function (e.g. hello world- option 1, goodbye world- option2, etc.)

    # Hello World option
    if answer == "1":
        my_function1()
        my_functionRestart()
        
    # Goodbye World option
    elif answer == "2":
        my_function2()
        my_functionRestart()

    # Goodbye Person option
    elif answer == "3":
        my_function3()
        my_functionRestart()
        
    # Good Teacher Option 
    elif answer == "4":
        my_function4()
        my_functionRestart()
       
    # For Loop option
    elif answer == "5":
        my_function5()
        my_functionRestart()
        
    # While Loop option    
    elif answer == "6":
        my_function6()
        my_functionRestart() 
    
    elif answer == "7":
        my_function7()
        my_functionRestart()
    
    elif answer == "8":
        my_function8()
        my_functionRestart()
    
    elif answer == "9":
        my_function9()
        my_functionRestart()

    # breaks the code
    elif answer == "x":
        my_functionX()

    # Invalid option
    else:
        my_functionInvalid()
        my_functionRestart()


# Defining functions for each set of code
def my_function1():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello World") 
    print("")
    print("----End of Output -----------------------------")

def my_function2():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
    print("")
    print("----End of Output -----------------------------")

def my_function3():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("Hello")
    username = input("What is your name ? ")
    print("Goodbye " + username)
    print("")
    print("----End of Output -----------------------------")
    

def my_function4():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    username = input("Teacher's name (try Mr Horan) ")
    x = "Mr Horan"

    if username == x:
        print("You are lucky, he is a great teacher.")
    else:
        print(username + " is an ok teacher")
    print("")
    print("----End of Output -----------------------------")

def my_function5():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    for x in range(1, 500):
        print(x)
    print("")
    print("----End of Output -----------------------------")

def my_function6():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    x = input("What is the name of this subject ")
    y = "IST"

    while x != y:
        print("Not Correct - try again")
        x = input("What is the name of this subject ")

    else: 
        print("")
        print("")
        print(" Congratulations!!")
        print("")
        print("")
    print("")
    print("----End of Output -----------------------------")

def my_function7():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    word = input("What is your string? ")
    for x in word:
        print(x)
    print("")
    print("----End of Output -----------------------------")
    
def my_function8():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    word = input("What is your string? ")

    for x in word:
        print(x, "=", ord(x))
    print("")
    print("----End of Output -----------------------------")
    
def my_function9 ():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    word = input("What is your string? ")
    ascii = ""

    for x in word:
        encode = chr(ord(x)+1)
        print(x, "=", encode)
        ascii += encode
        print(ascii)
    print("")
    print("----End of Output -----------------------------")

def my_functionX():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("")
    print("----End of Output -----------------------------")  
    print("")
    print("")
    print("")
    input("Press Enter to continue")


def my_functionInvalid():
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("invalid option")
    print("")
    print("----End of Output -----------------------------")

def my_functionRestart():
    print("")
    print("")
    print("")
    input("Press Enter to continue")
    return my_menu() # loop

my_menu() 



