myfile = open("readme.txt")
c = myfile.read()
for i in c:
    print(i)
c = c.splitlines()
print(c)
for i in c:
    print(i)
