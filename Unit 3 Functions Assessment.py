
def doubleeven(n):
    for n in range(2, 1000, 2):

    for n in range(1, 1000, 2):


print(doubleeven(int(input("enter int"))))

def functiongrade(percent):
    while percent <= 100 and percent >= 0:
        if percent <= 49:
            print("F")
        if percent > 65 and percent < 93:
            print("C")
        if percent >= 93:
            print("A+")
        elif percent >= 100 and percent <= 0:
            print("error")
