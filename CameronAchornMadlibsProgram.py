# Cameron Achorn's MadLibs Program

# These are the lists of the story's individual input words
space_words = [" name", " possessive pronoun (ex. his, her, their, etc.) for the name",
               " planet name", " singular object", ]
school_words = [" disease", " weapon", " past tense action verb", " present tense EPIC action verb"]
soccer_words = [" country", " another country", " silly first and last name",
                " first and last name that alliterate", " very serious but really cool first and last name",
                " past tense violent and aggressive action", " past tense gross action", " gross adjective"]


# This function calls the space story
def space():
    # Creates an empty list to store the words provided by the user
    input_words = []
    # For every word in the "space_words" list the user will have to go through and input their
    # own contributions to the story
    for word in space_words:
        user_input = input("Enter a" + word + ": ")
        input_words.append(user_input)

    # This variable is set so the function can return the space story and so if the variable is needed outside of main()
    global storySpace

    # This is the story with the input_words
    storySpace = "Little " + input_words[0] + " and " + input_words[1] + \
                 " astronaut crew were on an expedition to the planet " + input_words[2] + \
                 " when they encountered a(n) " + input_words[3] + ". The " + input_words[3] + \
                 " exploded and Little " + input_words[0] + " floated away into space."

    # This returns the story when the function is called
    return print(storySpace)


# This function calls the school story
def school():
    # Creates an empty list to store the words provided by the user
    input_words = []
    # For every word in the "school_words" list the user will have to go through and input their
    # own contributions to the story
    for word in school_words:
        user_input = input("Enter a" + word + ": ")
        input_words.append(user_input)

    # This variable is set so the function can return the space story and so if the variable is needed outside of main()
    global storySchool

    # This is the story with the input_words
    storySchool = "On a bright and shiny day at the " + input_words[0] + \
                  " preschool, two kids were fighting with " + input_words[1] + \
                  "s when the first kid " + input_words[2] + \
                  " on and through the second kid which made the first kid poop their pants. " \
                  "This caused the sun to " + input_words[3] + \
                  ", which resulted in night time. \"Fin.\""

    # This returns the story when the function is called
    return print(storySchool)


# This function calls the soccer story
def soccer():
    # Creates an empty list to store the words provided by the user
    input_words = []
    # For every word in the "soccer_words" list the user will have to go through and input their
    # own contributions to the story
    for word in soccer_words:
        user_input = input("Enter a" + word + ": ")
        input_words.append(user_input)

    # This variable is set so the function can return the space story and so if the variable is needed outside of main()
    global storySoccer

    # This is the story with the input_words
    storySoccer = "It is the world cup and it is " + input_words[0] \
                  + " facing " + input_words[1] + ". The star players from " + input_words[0] + " are " \
                  + input_words[2] + " and " + input_words[3] + ", and there is only one star player from " \
                  + input_words[1] + " named " + input_words[4] + ". These teams go head to head where " \
                  + input_words[4] + " scored 2 in the first half and " + input_words[2] + \
                  " scored 1 in the 90th minute. " + input_words[3] + \
                  " ends up getting a free kick due to being " + input_words[5] + ". " + input_words[3] + \
                  " missed the goal and after the game, " + input_words[3] + " had " + input_words[6] + \
                  " and was forever named " + input_words[3] + " the " + input_words[7] + "."

    # This returns the story when the function is called
    return print(storySoccer)


# If the global variables were needed outside of main they would be here
# These are here because python needs global variables to be used outside a function to be considered sanitized
storySpace = ""
storySchool = ""
storySoccer = ""

# User chooses a story they are interested in
choices = ["Space", "School", "Soccer"]


def main():
    # The make_story is to start and stop the while loop for the initial inputs
    make_story = input("Do you want make a story(\"Yes\" or \"No\")? ")

    # This while loop determines if the user inputs "Yes" or "No" and replays the sequence if it is not
    while make_story != "Yes" and make_story != "No":
        print("Sorry, please respond \"Yes\" or \"No\"")
        if make_story != "Yes" and make_story != "No":
            make_story = input("Do you want try another story(\"Yes\" or \"No\")? ")
        elif make_story == "No":
            break

    # The while loop is used to make sure the user inputs the correct keyword
    while make_story == "Yes":

        # This input statement is asking the user to input "Space", "School", or "Soccer"
        story_choice = input('Type "Space", "School", or "Soccer" to choose which story would '
                             'seem the most interesting to you: ')

        # The if statement is to see if the user's keyword matches the same keyword in the "choices" list
        if story_choice in choices:

            # if the keyword "Space" is typed, then the function space() is run
            if story_choice == "Space":
                space()

            # if the keyword "School" is typed, then the function school() is run
            elif story_choice == "School":
                school()

            # if the keyword "Soccer" is typed, then the function soccer() is run
            elif story_choice == "Soccer":
                soccer()

            # The make_story is to start and stop the while loop for the initial inputs
            make_story = input("Do you want try another story(\"Yes\" or \"No\")? ")

            # This while loop determines if the user inputs "Yes" or "No" and replays the sequence if it is not
            while make_story != "Yes" and make_story != "No":
                print("Sorry, please respond \"Yes\" or \"No\"")
                if make_story != "Yes" and make_story != "No":
                    make_story = input("Do you want try another story(\"Yes\" or \"No\")? ")
                elif make_story == "No":
                    break

        # This else statement is here to tell the user that there initial input was not one of the three keywords and
        # to input the keywords "Space", "School", or "Soccer" as they are shown
        else:
            print("This is not any of the choices as they are SPECIFICALLY displayed, try again!")


# Runs the function main()
main()
