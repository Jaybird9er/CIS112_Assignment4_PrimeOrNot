""" 
Author: Jamey Kirk
Title: Assignment4_Prime Number
Date: 03/14/2021
Description: program to identify a number is a prime number or not
"""

def primeOrNot(value):
    """
    identify whether input number is a prime number or not
    """
    pass

again = True

while (again):
    userNum = textinput("Please enter a number: ")
    playAgain = textinput("Do you want to play again? (Y or N) ")
    if (playAgain == "n" or playAgain == "N"):
        again = False