correct_password = "mikeshard"
password = input("Enter a Password: ")
passcount = 0
#bstring = "%s tries remaining, please try again:" % passnum

print(passcount, "hi")
while password != correct_password and passcount < 3:
    passnum = 3 - passcount

    bstring = "{} tries remaining, please try again:".format(passnum)
    password = input(bstring)
    passcount = passcount + 1


if password != correct_password:
    print("fuck off")
else:
    print("welcome")

print("hi", 3 - passcount, "you are logged in")

while password == correct_password and passcount <= 3:
    print("ii have sex with men")
    passcount = passcount + 1

print("done with loop")
