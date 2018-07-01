
def BigPrint(n):
    k = n
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k -= 1
        for b in range(0, i + 1):
            print("|", end="")
        print("\r")


num1 = int(input("how many lines do you want?: "))
if num1 == 10:
    print("suck huge dick!")
elif num1 > 10:
    print("SUCK A GIANT COCK")
else:
    print("your dicks small hehe xd")

BigPrint(num1)


def BigPrintF(n):

    for i in range(0, n):
        for j in range(0, i + 1):
            print("|", end="")
        print("\r")


BigPrintF(num1)


def calc_age(year):
    age = 2018 - year
    return age


print(calc_age(1854))
