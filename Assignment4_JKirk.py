""" 
Author: Jamey Kirk
Title: Assignment4_Prime Number
Date: 03/14/2021
Description: program to identify a number is a prime number or not
"""

def primeOrNot():
    """
    identify whether input number is a prime number or not
    """
    
    again = True
    while (again):
        userNum = int(input("Please enter a number: "))
        if (userNum / 2 % 2 == 1 or userNum / 2 % 2 == 0):
            print(userNum, "is not a prime number")
        else:
            print(userNum, "is a prime number")
        playAgain = input("Do you want to play again? (Y or N) ")
        if (playAgain == "n" or playAgain == "N"):
            again = False
            print("\nThank you for playing.")
        elif (playAgain == "y" or playAgain == "Y"):
            again = True

primeOrNot()