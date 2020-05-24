'''Contains Essential functions and classes for solving other problems

Copyright © 2020 PranavAnand587. All rights reserved. 

https://github.com/PranavAnand587/PyEuler

Euler problems - https://projecteuler.net/archives

'''


# Function for converting all answers to a list
def answersList():
    # Reads the answers file
    file = open("Answers.txt", "r")
    data = file.readlines()

    answers = []
    for line in data:
        answers = line.split()

    return answers


answersList()

# Function for Calculating Digits in a Number


def DigitsNum(num):
    digits = 0

    # loops through as long as the given number is 0
    while(num > 0):
        num//10  # removes last digit
        digits += 1

    return digits
