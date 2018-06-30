x = b'yeehaw'
print(x)
print(type(x))
print(str(10.09))
array1 = ["happy", "sad", "gay", "cool", "c00cky!"]
print(array1[1: 3])
array1.append("Lovely")
print(array1[-1])


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

BigPrint(num1)


def BigPrintF(n):

    for i in range(0, n):
        for j in range(0, i + 1):
            print("|", end="")
        print("\r")


BigPrintF(num1)
