#!/usr/bin/python2

from __future__ import print_function
import time
import sys

####  TODO
# 
# - Set up whole game flow.
# - Create problems for easy, medium and hard.
# - Check for function with more than 18 lines.



# ******************************************************************************
#
# HELPER FUNCTIONS
# 
# ******************************************************************************


def print_line(char="-"):
    """Prints 80 repetitions of a defined character to create a line. 
    Default is '-'."""
    print(80*char)
    return None


def isnumber(num):
    """Tests is the input can be turned into a float. If yes returns True, 
    otherwise returns False."""

    # float() can only handle numbers (int, float) and strings as inputs. 
    # Therefore, testing if input is one of these types.
    if isinstance(num, (str, float, int)):
        try:
            float(num)
        except ValueError:
            return False
        else: 
            return True
    else:
        return False



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
    print_line(char="#")
    title = "### Fill in the ____ ###"
    title_max_index = len(title) + 1
    fix_first_index = 16

    # print title forward with gap
    for i in range(1, title_max_index):
        print_overwritable_slice(string_to_print=title, slice_end=i)
        time.sleep(0.1)
    
    # wait (like recognizing that there is something wrong in the title.)
    time.sleep(0.5)
    
    # remove "typo"
    for i in range(title_max_index, fix_first_index, -1):
        clear_line(len(title))
        print_overwritable_slice(string_to_print=title, slice_end=i)
        time.sleep(0.1)
    
    # print fixed title
    title = "### Fill in the Gaps ###"
    for i in range(fix_first_index, title_max_index, 1):
        print_overwritable_slice(string_to_print=title, slice_end=i)
        time.sleep(0.1)
    print("")
    print_line(char="#")
    print("")

    
    return None



# ******************************************************************************
#
# USER OPTIONS
# 
# ******************************************************************************


def select_difficulty():
    """Promts the user to select a difficulty level (easy, medium or hard) and 
    returns the selected level as string. If the user input does not match one 
    of the options, the input is requested again."""
    user_level = ""
    possible_levels = ["easy", "medium", "hard"]
    while user_level not in possible_levels:
        user_level = raw_input("Which difficulty level do you want to play? "
            "Possible choices: {}\n".format(possible_levels))
        if user_level not in possible_levels:
            print("Sorry, that is not a valid level. Try again.\n")
    print("Ok, it's going to be {}.\n".format(user_level))
    return user_level


def select_wrong_guesses():
    """Promts the user to select a number of possible wrong guesses or to just 
    hit [Enter] for the default value of 3. Returns the selected number of 
    possible wrong guesses as an integer."""
    user_limit = ""
    default_limit = 3
    while not isnumber(user_limit):
        user_limit = raw_input("How may wrong guesses do you want to be allowed?"
            " (Hit [Enter] for default = {}): ".format(default_limit))
        if user_limit == "":
            user_limit = default_limit
        if not isnumber(user_limit):
            print("Sorry, that is not a valid number of wrong guesses. Try again.\n")
    user_limit = int(float(user_limit))
    print("Ok, you are granted {} wrong guesses to solve the quiz.\n".format(user_limit))
    return user_limit



# ******************************************************************************
#
# GAME
# 
# ******************************************************************************


def print_phrase(phrase):
    """Prints the problem phrase in between two lines (for accent)."""
    print("Phrase:")
    print_line()
    print(phrase)
    print_line()
    return None


def print_final_state(phrase):
    """Prints the final state of problem phrase in between two lines of stronger
    accent."""
    print("Final State:")
    print_line(char="=")
    print(phrase)
    print_line(char="=")
    return None    


def replace_case_sensitive(phrase, placeholder, replacement):
    """Takes in a phrase (possibly conisting of multiple sentences), a placeholder
    and its replacement. Each occurence of the placeholder will be replaced with
    the replacement. If the placeholder is first word in phrase of sentence, the
    replacement is capitalized. 
    The phrase with placeholders replaced will be returned."""

    while placeholder in phrase:
        placeholder_index = phrase.find(placeholder)

        is_first_word_of_phrase = placeholder_index == 0
        is_first_word_of_sentence = placeholder_index >= 2 \
            and phrase[placeholder_index - 2] in ".!?"

        if is_first_word_of_phrase or is_first_word_of_sentence:
            # If placeholder is first word in phrase or sentence, its replacement
            # should be capitalized.
            phrase = phrase.replace(placeholder, replacement.capitalize(), 1)
        else:
            # Otherwise, the replacement can be used as is.
            phrase = phrase.replace(placeholder, replacement, 1)

    return phrase


def end_of_game(wrong_guesses_counter, wrong_guesses_limit, placeholder_index, 
    max_placeholder_index):
    """Determines if game was won or lost and prints a fitting message 
    accordingly. Needs counter and limit for wrong guesses and current and 
    maximum placeholder index as inputs."""

    if wrong_guesses_counter > wrong_guesses_limit:
        print("You have reached the limit of wrong guesses!\n")
    elif placeholder_index > max_placeholder_index:
        print("Congratulations. You have filled all the gaps correctly.\n")
    else:
        print("This is odd. The game is over, but I  don't know why!?\n")
    
    print_line(char="#")
    print("### GAME OVER ###")    
    print_line(char="#")
    print("")
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

        print_phrase(problem_phrase)
        user_answer = raw_input("What do you think fits {}? ".format(placeholder))

        if user_answer.lower() == answer.lower(): # checking case insensitive
            print("Correct!")
            problem_phrase = replace_case_sensitive(problem_phrase, placeholder, 
                answer)
            placeholder_index += 1
        else:
            print("Sorry, but '{}' does not fit {}.".format(user_answer, 
                placeholder))
            wrong_guesses_counter += 1
            if wrong_guesses_counter <= wrong_guesses_limit:
                print("Try again!\n")

    print("")
    print_final_state(problem_phrase)

    # The game is over. 
    # Time to tell the player how it ended.
    end_of_game(wrong_guesses_counter, wrong_guesses_limit, placeholder_index, 
        max_placeholder_index)

    return None



# ******************************************************************************
#
# RUN
# 
# ******************************************************************************


if __name__ == "__main__":
    
    fill_in_the_gaps_title()

    difficulty = select_difficulty()

    limit = select_wrong_guesses()

    play_game(
        problem_phrase = "This is a __1__.", 
        list_of_tuples_placeholder_and_answer = [
            ("__1__", "test")
            ], 
            wrong_guesses_limit = limit
            )
