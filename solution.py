'''This program gives the solution of any Euler Project Problem when given the problem number

Copyright © 2020 PranavAnand587. All rights reserved. 

https://github.com/PranavAnand587/PyEuler

Euler problems - https://projecteuler.net/archives

'''

import eulerlib as lib

logo = '''

========================================================================                                                                         
88888888ba              88888888888            88                        
88      "8b             88                     88                        
88      ,8P             88                     88                        
88aaaaaa8P' 8b       d8 88aaaaa    88       88 88  ,adPPYba, 8b,dPPYba,  
88""""""'   `8b     d8' 88"""""    88       88 88 a8P_____88 88P'   "Y8  
88           `8b   d8'  88         88       88 88 8PP""""""" 88          
88            `8b,d8'   88         "8a,   ,a88 88 "8b,   ,aa 88          
88              Y88'    88888888888 `"YbbdP'Y8 88  `"Ybbd8"' 88          
                d8'                                                      
               d8'                                                   
=========================================================================

        Copyright © 2020 PranavAnand587. All rights reserved. 

=========================================================================
'''

prompt = '''Note -  Each Problem No should be written as a Number.
        For example => Problem 1 = 1 or Problem 256 = 256
 
Enter the Problem Number Here = '''


def Start():
    answersList = lib.answersList()

    inp = str(input(prompt))

    if inp.isnumeric():
        print(
            f"\nThe solution to the Problem {inp} is : {answersList[int(inp)-1]}")
        Start()
    elif inp == 0:
        print("\nThanks for trying!!!\nPlease star my the repo in github:")
    else:
        print("\nPrint a Valid Problem No according to format specified\n")
        inp = str(input(prompt))


if __name__ == '__main__':
    print(logo)
    Start()
