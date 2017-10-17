#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""Play a fill-in-the-gaps game."""

from __future__ import print_function
import time
import sys


# ******************************************************************************
#
# HELPER FUNCTIONS
# 
# ******************************************************************************


def print_line(char="-"):
    """
    Print 80 repetitions of a defined character to create a line. Return None.

    Input:
    char -- Character used to create the line. Default is '-'.
    """

    print(80*char)
    return None


def isnumber(num):
    """
    Test if input can be turned into a number/float. Return True or False.

    Input has to be string, integer or float. In all other cases return False."""

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
    """
    Print an overwritable slice of a string. Return None.

    Inputs:
    string_to_print -- The string of which the slice will be printed.
    slice_end -- Index of the end of the slice to be printed.

    After printing the definied slice, the cursor returns to the beginning of the 
    line to enable overwriting.
    """

    sys.stdout.write("\r" + string_to_print[:slice_end])
    sys.stdout.flush()
    return None


def clear_line(length):
    """
    Print an overwritable empty line of a defined length. Return None.

    Input:
    length -- Length of line/number of spaces to be printed.

    After printing the definied line, the cursor returns to the beginning of the 
    line to enable overwriting.
    """

    sys.stdout.write("\r" + " "*length)
    sys.stdout.flush()    
    return None


def typing_print(typing_string , from_index = 0, to_index = None, step = 1, 
        delay = 0.1):
    """
    Print a string one character at a time to simulate typing. Return None.

    Inputs:
    typing_string -- String to be printed in typing style.
    from_index -- First index of string to be printed in typing style. Default = 0.
    to_index -- Last index of string to be printed in typing style. 
        Default = end of string.
    step -- Number of characters printed at the same time. Default = 1.
    delay -- Time in seconds between print of each step/character. Default = 0.1.

    Cursor returns to beginning of line after printing is done. To avoid overwriting, 
    print an empty string afterwards.
    """

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
    """
    Promt user to select a difficulty level. Return user's selection.

    Print message to user to select a difficulty level ["easy", "medium", "hard"].
    If user input is not a valid level, inform user of wrong input and promt
    request again.
    """

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
    """
    Promt user to select a number of possible wrong guesses. Return user's selection.

    Print message to user to select a number of possible wrong guesses. 
    Also, offer to just hit [Enter] for the default number of 3 wrong guesses. 
    If user input is not a number, inform user of wrong input and promt
    request again.    
    """

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
    """
    Take level string and return quiz dictionary with phrase, placeholders and answers.

    Input:
    level -- String defining the quiz to be returned. Possible levels "easy", 
        "medium", "hard".

    Output:
    Dictionary containing the "phrase" and a list of tuples containing the 
    "placeholders_and_answers". Each list entry is a tuple, containing the 
    placeholder at index 0 and the correct replacement at index 1.
    If level not available return None.
    """

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
    if level in quiz:
        return quiz[level]
    else:
        return None


# ******************************************************************************
#
# GAME
# 
# ******************************************************************************


def print_phrase(phrase):
    """
    Print the problem phrase in between two lines. Return None.

    Input:
    phrase -- String to be printed in between two horizontal lines. The horizontal
        lines act as emphasis to the printed phrase and separate it from other
        surrounding lines.
    """

    print("")
    print("Phrase:")
    print_line()
    print(phrase)
    print_line()
    return None


def print_final_state(phrase):
    """
    Print the final state of problem phrase in between two strong lines. Return None.
    
    Input:
    phrase -- String to be printed in between two horizontal lines. The horizontal
        lines act as emphasis to the printed phrase and separate it from other
        surrounding lines.
    """

    print("")
    print("Final State:")
    print_line(char="=")
    print(phrase)
    print_line(char="=")
    return None    


def get_user_answer(phrase, placeholder):
    """
    Print phrase with placeholder and ask user to fill the placeholder. 

    Input:
    phrase -- Quiz phrase/string containing placeholder(s).
    placeholder -- Placeholder string occuring in the phrase the user is asked
        to replace.
    
    Output:
    The user's answer string (supposed to replace the placeholder).
    """

    print_phrase(phrase)
    user_answer = raw_input("What do you think fits {}? ".format(placeholder))
    return user_answer



def replace_case_sensitive(phrase, placeholder, replacement):    
    """
    Replace a placeholder in the phrase with it's replacement with respect to case.

    Inputs:
    phrase -- Quiz phrase/string containing placeholder(s).
    placeholder -- Placeholder string occuring in the phrase which is to be
        replaced.
    replacment -- Replacement for the placeholder. 

    Outputs: 
    Phrase in which all occurrences of the placeholder replaced with the replacement
    using the correct case.

    If an occurrence of the placeholder is the first word in the phrase or in a
    sentence, the replacement will be capitalzed. 
    In any other position the replacement is used as defined in the input.
    """

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
    """
    Determine if game was won or lost and print a fitting message. Return None.

    Inputs: 
    problem_phrase -- Final state of phrase the user has tried to solve.
    wrong_guesses_counter -- Number of wrong guesses the user has made, while
        trying to solve the quiz.
    wrong_guesses_limit -- Maximum number of wrong guesses the user was allowed
        to have while trying to solve the quiz.
    placeholder_index -- Index of the placeholder the user would be supposed to
        replace.
    max_placeholder_index -- Maximum index of placeholders the user can be asked
        to replace.

    Print final state of quiz phrase and a message showing if the user has won
    or lost the game. 
    If the user needed more wrong guesses than allowed, then the user lost.
    If the user would be asked to fill a placeholder index higher than the maximum
    possible, the user has filled all gaps and won.
    Print 'game over' message.
    """

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
    """
    Start a fill-in-the-gaps game. Return None.

    Inputs:
    problem_phrase -- Quiz phrase/string containing placeholder(s).
    list_of_tuples_placeholder_and_answer -- List containing tuples, with each
        tuple containing a placeholder occurring in the phrase at index 0 and
        the correct replacement for that placeholder at index 1.
    wrong_guesses_limit -- Integer defining how many wrong guesses the user is 
        allowed to make while trying to replace all placeholders.

    Print the problem phrase and ask the user to give a replacement for a specific
    placeholder. 
    If the user input corresponds to the defined replacement (case insensitive)
    replace the placeholder with the correct answer (case sensitive). Print the
    phrase with the placeholder replaced and ask the user to replace the next 
    placeholder.
    If the user input does not correspond to the defined replacement, inform the
    user about the wrong answer and ask to fill the placeholder again. 
    The game ends if all placeholders are replaced or more wrong guesses have been
    made than allowed. Print corresponding message.
    """

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
