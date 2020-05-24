'''Solution to Problem 1 : Multiples of 3 and 5 

Copyright © 2020 PranavAnand587. All rights reserved. 

https://github.com/PranavAnand587/PyEuler

Euler problems - https://projecteuler.net/archives

'''


def solve():
    # One liner for calculating sums of muliples of 3 and 5 upto 1000
    # I have used sum function and lisr comprehension here
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return ans


if __name__ == '__main__':
    print(f"Solution to Problem 1 = {solve()}")
