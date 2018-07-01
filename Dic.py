import json
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Try Again, word doesnt exist:  "


def again():
    choice = input("Do you want to translate again? Y or N : ")
    print("\n")
    while choice == "Y":
        user_word2 = input("Type the other word you want to translate: ")
        output2 = translate(user_word2)
        if type(output2) == list:
            for item in output2:
                print(item)
            print("\n")
        else:
            print(output2)
            print("\n")
        choice = input("Again? Y or N:  ")


user_word = input("Enter a word to translate: ")
output = translate(user_word)
if type(output) == list:
    for item in output:
        print(item)
    print("\n")
    again()
else:
    print(output)
    print("\n")
    again()
print("have a nice day")
