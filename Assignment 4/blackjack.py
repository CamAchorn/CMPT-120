# if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
# this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust:
add these three numbers together. if they add up to or less than 21, return the sum.
If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random

def bust():
    x = 0
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    a =random.choice(list1)
    y =random.choice(list1)
    z =random.choice(list1)
    x = a + y + z
    # This print statement is to see the values being randomized
    print(a, y, z)
    if (x <= 21):
        return x
    if (x > 21 and a==11 or y==11 or z==11):
        return (x - 10)
    if (x > 21):
        return 0

def main():
    print(bust())

main()
