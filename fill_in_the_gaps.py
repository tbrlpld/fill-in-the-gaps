#!/usr/bin/python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
import sys


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


def typing_print(typing_string , from_index = 0, to_index = None, step = 1, 
        delay = 0.1):
    """Takes in a string and prints the letters one by one to simulate typing. 
    The part of the string to be typed can be defined with the optional arguments
    from_index and to_index. Also, the step size and the typing delay can be 
    defined with optional arguments. Returns None.
    Attention: The cursor remains at the beginning of the line printed. To avoid
    overwriting, print an empty string afterwards."""

    # If to_index was not defined explicitly it is None. This has to be turned
    # into something useful, like the maximum possible index.
    if to_index == None:
        to_index = len(typing_string)

    range_end_modifier = step/abs(step)

    for end_of_slice_printed in range(from_index, 
            to_index + range_end_modifier, step):
        clear_line(len(typing_string))
        print_overwritable_slice(string_to_print=typing_string, 
            slice_end=end_of_slice_printed)
        time.sleep(delay)

    return None


def fill_in_the_gaps_title():
    """Print an animated title for the game."""
    print("")
    print_line(char="#")
    title = "### Fill in the ____ ###"
    title_max_index = len(title)
    fix_first_index = 16

    # print title forward with gap
    typing_print(typing_string = title, from_index = 0, to_index = title_max_index, 
        step = 1, delay = 0.1) 
   
    # wait (like recognizing that there is something wrong in the title.)
    time.sleep(0.5)
    
    # remove "typo"
    typing_print(typing_string = title, from_index = title_max_index, 
        to_index = fix_first_index, step = -1, delay = 0.1) 

    # print fixed title
    title = "### Fill in the Gaps ###"
    typing_print(typing_string = title, from_index = fix_first_index, 
        to_index = title_max_index, step = 1, delay = 0.1) 

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
            "Possible choices: {}\n".format(possible_levels)).lower()
        if user_level not in possible_levels:
            print("Sorry, that is not a valid level. Try again.\n")
    print("Ok, it's going to be {}.".format(user_level))
    print("")
    return user_level


def select_wrong_guesses():
    """Promts the user to select a number of possible wrong guesses or to just 
    hit [Enter] for the default value of 3. Returns the selected number of 
    possible wrong guesses as an integer."""
    user_limit = ""
    default_limit = 3
    while not isnumber(user_limit):
        user_limit = raw_input("How many wrong guesses do you want to be allowed?"
            " (Hit [Enter] for default = {}): ".format(default_limit))
        if user_limit == "":
            user_limit = default_limit
        if not isnumber(user_limit):
            print("Sorry, that is not a valid number of wrong guesses. Try again.\n")
    user_limit = int(float(user_limit))
    print("Ok, you are granted {} wrong guesses to solve the quiz.".format(user_limit))
    return user_limit


# ******************************************************************************
#
# QUIZ PHRASES
# 
# ******************************************************************************


def get_quiz(level):
    """Takes in a level string (easy, medium or hard) and returns a dictionary 
    containing the associated problem phrase and the list of tuples (containing 
    the placeholders and answers)."""
    quiz = {
        "easy": {
            "phrase": "The president of the United States of America in 2017 is Donald __1__. Before __1__ it was __2__ Obama. __2__ Obama's predecessor was George W. __3__. George W. __3__ followed Bill Clinton in the __4__ office.",
            "placeholders_and_answers": [("__1__", "Trump"), ("__2__", "Barack"), ("__3__", "Bush"), ("__4__", "oval")]
        },
        #
        "medium": {
            "phrase": "How much __1__ __2__ a __3__ chuck if a __3__ __4__ chuck __1__?",
            "placeholders_and_answers": [("__1__", "wood"), ("__2__", "would"), ("__3__", "woodchuck"), ("__4__", "could")]
        },
        #
        "hard": {
            "phrase": "Dihydrogen monoxide is commonly known as __1__. __1__ boils at temperatures above __2__°C and freezes at temperatures below __3__°C. Frozen __1__ is called __4__.",
            "placeholders_and_answers": [ ("__1__", "water"), ("__2__", "100"), ("__3__", "0"), ("__4__", "ice")]
        }
    }
    return quiz[level]


# ******************************************************************************
#
# GAME
# 
# ******************************************************************************


def print_phrase(phrase):
    """Prints the problem phrase in between two lines (for accent)."""
    print("")
    print("Phrase:")
    print_line()
    print(phrase)
    print_line()
    return None


def print_final_state(phrase):
    """Prints the final state of problem phrase in between two lines of stronger
    accent."""
    print("")
    print("Final State:")
    print_line(char="=")
    print(phrase)
    print_line(char="=")
    return None    


def get_user_answer(phrase, placeholder):
    """Print phrase with placeholder and ask user to fill the placeholder. 
    Returns the user's answer."""

    print_phrase(phrase)
    user_answer = raw_input("What do you think fits {}? ".format(placeholder))
    return user_answer



def replace_case_sensitive(phrase, placeholder, replacement):
    """Takes in a phrase (possibly conisting of multiple sentences), a placeholder
    and its replacement. Each occurence of the placeholder will be replaced with
    the replacement. If the placeholder is first word in phrase of sentence, the
    replacement is capitalized. 
    The phrase with placeholders replaced will be returned."""

    while placeholder in phrase:
        placeholder_index = phrase.find(placeholder)

        is_first_word_of_phrase = placeholder_index == 0
        # Offset to phrase start necessary to be able to not check the end of 
        # the phrase (negative indexes) when checking for possible sentence ends.
        offset_to_last_sentence_end = 2
        min_offset_to_phrase_start = offset_to_last_sentence_end 
        is_first_word_of_sentence = placeholder_index >= min_offset_to_phrase_start \
            and phrase[placeholder_index - offset_to_last_sentence_end] in ".!?"

        if is_first_word_of_phrase or is_first_word_of_sentence:
            # If placeholder is first word in phrase or sentence, its replacement
            # should be capitalized.
            phrase = phrase.replace(placeholder, replacement.capitalize(), 1)
        else:
            # Otherwise, the replacement can be used as is.
            phrase = phrase.replace(placeholder, replacement, 1)

    return phrase


def end_of_game(problem_phrase, wrong_guesses_counter, wrong_guesses_limit, 
    placeholder_index, max_placeholder_index):
    """Determine if game was won or lost and print a fitting message. 

    Needs counter and limit for wrong guesses and current and maximum 
    placeholder index as inputs."""

    print_final_state(problem_phrase)

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
    max_placeholder_index = len(list_of_tuples_placeholder_and_answer) - 1

    # Play as long as not all placeholders are replaced and the wrong guesses 
    # limit is not reached.
    while wrong_guesses_counter <= wrong_guesses_limit and placeholder_index <= max_placeholder_index:

        placeholder = list_of_tuples_placeholder_and_answer[placeholder_index][0]
        answer = list_of_tuples_placeholder_and_answer[placeholder_index][1]

        user_answer = get_user_answer(problem_phrase, placeholder)
        
        if user_answer.lower() == answer.lower(): # checking case insensitive
            print("Correct!")
            problem_phrase = replace_case_sensitive(problem_phrase, placeholder, answer)
            placeholder_index += 1
        else:
            print("Sorry, but '{}' does not fit {}.".format(user_answer, placeholder))
            wrong_guesses_counter += 1
            if wrong_guesses_counter <= wrong_guesses_limit:
                print("Try again!")

    # The game is over. 
    # Time to tell the player how it ended.
    end_of_game(problem_phrase, wrong_guesses_counter, wrong_guesses_limit, placeholder_index, max_placeholder_index)

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
    quiz = get_quiz(difficulty)
    play_game(
        problem_phrase = quiz["phrase"],
        list_of_tuples_placeholder_and_answer = quiz["placeholders_and_answers"],
        wrong_guesses_limit = limit
        )
