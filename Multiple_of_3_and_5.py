"""
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Courtesy of ProjectEuler.net
"""
def solution(number):
    number = number - 1
    l = []
    while number>0:
        if number % 3 ==0 or number%5==0:
            l.append(number)
        number-=1
    return sum(l)
