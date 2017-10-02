#!/usr/bin/python2

from __future__ import print_function
import time
import sys

# ******************************************************************************
#
# TITLE
# 
# ******************************************************************************

def print_overwritable_slice(string_to_print, slice_end):
    """Prints a string to a defined slice end, and places the cursor at the 
    beginning of the line, to enable overwriting."""
    sys.stdout.write("\r" + string_to_print[:slice_end])
    sys.stdout.flush()
    return None


def clear_line(length):
    """Prints a given number of spaces (basically an empty line). The cursor is
    placed back at the beginning of the line to be overwritten."""
    sys.stdout.write("\r" + " "*length)
    sys.stdout.flush()    
    return None


def fill_in_the_gaps_title():
    """Print an animated title for the game."""
    print("")
    title = "### Fill in the ____ ###"
    title_max_index = len(title) + 1
    fix_first_index = 16

    # print title forward with gap
    for i in range(1, title_max_index):
        print_overwritable_slice(string_to_print=title, slice_end=i)
        time.sleep(0.2)
    
    # wait (like recognizing that there is something wrong in the title.)
    time.sleep(1)
    
    # remove "typo"
    for i in range(title_max_index, fix_first_index, -1):
        clear_line(len(title))
        print_overwritable_slice(string_to_print=title, slice_end=i)
        time.sleep(0.2)
    
    # print fixed title
    title = "### Fill in the Gaps ###"
    for i in range(fix_first_index, title_max_index, 1):
        print_overwritable_slice(string_to_print=title, slice_end=i)
        time.sleep(0.2)
    print("\n")
    
    return None

# ******************************************************************************
#
# GAME
# 
# ******************************************************************************

def end_of_game(wrong_guesses_counter, wrong_guesses_limit, placeholder_index, 
    max_placeholder_index):
    """Determines if game was won or lost and prints a fitting message 
    accordingly. Needs counter and limit for wrong guesses and current and 
    maximum placeholder index as inputs."""

    if wrong_guesses_counter > wrong_guesses_limit:
        print("You have reached the limit of wrong guesses!")
    elif placeholder_index > max_placeholder_index:
        print("Congratulations. You filled all the gaps correctly.")
    else:
        print("This is odd. The game is over, but I  don't know why!?")
    
    print("")
    print("### GAME OVER ###")    

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
    end_of_game(wrong_guesses_counter, wrong_guesses_limit, placeholder_index, 
        max_placeholder_index)

    return None




