def main():
    # good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")

    # can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isnumeric():
        print("int!")
    else:
        print("not int :(")

    # what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalpha() and alphIntInput.isnumeric():
        print("Letters and numbers!")
    else:
        print("weird characters :(")

    # good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")

    # now write code to check if the input was either an asterisk OR an ampersand (&)
    astersand = input("Enter an asterisk or ampersand please")
    if astersand == "*" or astersand == "&":
        print("good!")
    else:
        print("not asterisk :(")
    # do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    intI = input("enter an int")
    if intI.isnumeric():
        print("int!")
    else:
        print("not int :(")

    # last challenge: find out how to check if the string input has the substring "marist"
    word = input("enter a string.")
    if (word.find('marist') == 6):
        print("the word 'marist' is in the phrase")

    # google this one ;) substring is the key google term


main()