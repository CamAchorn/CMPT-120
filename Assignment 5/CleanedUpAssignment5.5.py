# This is the cleaned up version of assignment 3 "if_else_loop_practice"

def main():
    list1 = [2, 13, 42, 9, 26]

    # This for loop goes through each number in the list to test if it is higher or lower than certain values
    for x in range(len(list1)):

        # if value is greater than 35 it prints "greater than 35"
        if list1[x] > 35:
            print("greater than 35")

        # if value is between 20 and 35 then it prints "between 20-35"
        elif 35 > list1[x] > 20:
            print("between 20-35")

        # if value is between 5 and 20 then it prints "between 5-20"
        elif 20 > list1[x] > 5:
            print("between 5-20")

        # if the value is less than 5 then it prints "the number is less than 5"
        else:
            print("the number is less than 5")


main()
