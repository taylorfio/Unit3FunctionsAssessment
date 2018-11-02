import random


def doubleeven(n):
    if n in range(2, 1000, 2):
        n = n * 2
        return n
    if n in range(1, 1000, 2):
        n = -1
        return n
    elif n < 0:
        return"error"


print(doubleeven(int(input("enter +int"))))


def functiongrade(percent):
    if percent >= 0 and percent <= 49:
        return ("F")
    if percent > 49 and percent < 65:
        return ("C")
    if percent >= 65 and percent < 93:
        return("B")
    if percent >= 93 and percent <= 100:
        return("A+")
    elif percent >= 100 or percent <= 0:
        return ("error")


print(functiongrade(int(input("enter grade"))))


def largestnum(num1, num2, num3):
    if num1 > num2 and num3:
        return num1
    if num2 > num3 and num1:
        return num2
    if num3 > num2 and num1:
        return num3


print(largestnum(1, 2, 3))


def sum_dice(dice, numrolls):
    sum = 0
    for x in range(1, numrolls):
        num_holder = random.randint(1, dice)
        sum = sum + num_holder
    return sum


print(sum_dice(6, 5))

