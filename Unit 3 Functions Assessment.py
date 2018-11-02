def doubleeven(n):
    if n (2, 1000, 2):
        n = n * 2
        return n
    if n (1, 1000, 2):
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

