ifnum = 50
if ifnum == 10:
    print("The value of ifnum variable is 10, so condition is true!")
    print("The value of ifnum variable is = " + str(ifnum))
else:
    print("The ifnum variable value is other than 10!")
num = 10
if num <= 5:
    print(num + 5)
else:
    print(5*2 == 5.0 * 2.0)
for i in range(0, 10):
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")


def pyramid(n):
    for i in reversed(range(0, n)):
        for x in range(0, i+1):
            print("* ", end="")
        print("\r")


n = int(input("Enter any Number before i suck your sock: "))
pyramid(n)
