#!/usr/bin/python3

import time

print("### Fill in the Gaps ###")

def typewriter_print(string_to_print):
    for i in range(1, len(string_to_print) + 1):
        print("\r" + string_to_print[:i], end="")
        time.sleep(0.5)

def fill_in_the_gaps_title():
    """Print an animated title for the game."""
    print("\n")
    title = "### Fill in the ____ ###"
    title_max_index = len(title) + 1
    fix_first_index = 16
    for i in range(1, title_max_index):
        print("\r" + title[:i], end="")
        time.sleep(0.1)
    # print("")
    # print("")   
    for i in range(title_max_index, fix_first_index, -1):
        print("\r" + " " * len(title), end="")
        print("\r" + title[:i], end="")
        # print(title[:i])
        time.sleep(0.3)
    # print("")
    title = "### Fill in the Gaps ###"
    for i in range(fix_first_index, title_max_index, 1):
        print("\r" + title[:i], end="")
        time.sleep(0.1)
    print("\n")
    return None


def play_game(problem_phrase, list_of_tuples_placeholder_and_answer, wrong_guesses_limit):
    """This is the main function to play the fill-in-the-gaps game. It takes the
    problem phrase (the text with the gaps), a list of tuples and the maximum
    number of wrong guesses as inputs. 
    Each tuple in the list has to contain the placeholder (used in the problem 
    phrase) and it's correct replacement.
    This function always returns None."""
    wrong_guesses_counter = 0
    placeholder_index = 0
    max_placeholder_index =  len(list_of_tuples_placeholder_and_answer) - 1

    # Play as long as not all placeholders are replaced and the wrong guesses 
    # limit is not reached.
    while wrong_guesses_counter <= wrong_guesses_limit \
        and placeholder_index <= max_placeholder_index:

        placeholder = list_of_tuples_placeholder_and_answer[placeholder_index][0]
        answer = list_of_tuples_placeholder_and_answer[placeholder_index][1]

        print(problem_phrase)
        user_answer = raw_input("What do you think fits {}? ".format(placeholder))

        if user_answer == answer:
            print("Correct!")
            problem_phrase = problem_phrase.replace(placeholder, answer)
            placeholder_index += 1
        else:
            print("Sorry, but '{}' does not fit {}.".format(user_answer, placeholder))
            wrong_guesses_counter += 1

    # The game is over. 
    # Time to tell the player how it ended.
    if wrong_guesses_counter > wrong_guesses_limit:
        print("You have reached the limit of wrong guesses!")
    elif placeholder_index > max_placeholder_index:
        print("Congratulations. You filled all the gaps correctly.")
    else:
        print("This is odd. The game is over, but I  don't know why!?")

    print("")
    print("### GAME OVER ###")

    return None


print("###################")
print("Testing")
print("###################")

# print("")
# print("Testing play_game() - 1")
# print("")
# play_game(
#     problem_phrase="This is a __1__.", 
#     wrong_guesses_limit=1, 
#     list_of_tuples_placeholder_and_answer=[("__1__","placeholder")])


# print("")
# print("Testing play_game() - 2")
# print("")
# play_game(
#     problem_phrase="This is a __1__. And that's another __2__.", 
#     wrong_guesses_limit=1, 
#     list_of_tuples_placeholder_and_answer=[
#         ("__1__","placeholder"),
#         ("__2__","gap")
#         ])

print("")
print("Testing fill_in_the_gaps_title() - 1")
print("")
fill_in_the_gaps_title()

