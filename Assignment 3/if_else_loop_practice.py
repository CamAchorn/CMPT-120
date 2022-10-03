# first of all, breathe
# don't let this intimidate you. break it down a part at a time. You've done all of these separately and now we're just combining them.
'''
Instructions: Create a list with at least 8 numbers, and make sure you have a raandom dispersement between 0-50
Create a loop (which loop would be best given we know how long we're going [the length of the list]?) that runs through the entire list
Inside of your loop, have an if/elif/else that checks AT EACH INDEX OF THE LIST:
if the number is greater than 35: print ("greater than 35")
elif the number is between 20-35: print ("between 20-35")
elif the number is between 5-20: print ("between 5 and 20")
else (the number is less than 5)
'''


def main():
    rcf = [2,13,42,9,26]

    for x in range(len(rcf)):
        if rcf[x] > 35:
            print("greater than 35")
        elif rcf[x] < 35 and rcf[x] > 20:
            print("between 20-35")
        elif rcf[x] < 20 and rcf[x] > 5:
            print("between 5 and 20")
        else:
            print("the number is less than 5")

main()
