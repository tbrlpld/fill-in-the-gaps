
from fill_in_the_gaps import play_game

print("###################")
print("Testing")
print("###################")

print("")
print("Testing play_game() - 1")
print("")
play_game(
    problem_phrase="This is a __1__.", 
    wrong_guesses_limit=1, 
    list_of_tuples_placeholder_and_answer=[("__1__","placeholder")])


print("")
print("Testing play_game() - 2")
print("")
play_game(
    problem_phrase="This is a __1__. And that's another __2__.", 
    wrong_guesses_limit=1, 
    list_of_tuples_placeholder_and_answer=[
        ("__1__","placeholder"),
        ("__2__","gap")
        ])