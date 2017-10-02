
from fill_in_the_gaps import play_game

print("###################")
print("Testing")
print("###################")


# print("Testing play_game() - 1")
# play_game(
#     problem_phrase="This is a __1__.", 
#     wrong_guesses_limit=1, 
#     list_of_tuples_placeholder_and_answer=[("__1__","placeholder")])



# print("Testing play_game() - 2")
# play_game(
#     problem_phrase="This is a __1__. And that's another __2__.", 
#     wrong_guesses_limit=1, 
#     list_of_tuples_placeholder_and_answer=[
#         ("__1__","placeholder"),
#         ("__2__","gap")
#         ])

print("Testing play_game() - 3")
play_game(
    problem_phrase="This is a __1__. __2__ need to be filled, because this game " +
        "is called 'fill the __2__'.", 
    wrong_guesses_limit=1, 
    list_of_tuples_placeholder_and_answer=[
        ("__1__","placeholder"),
        ("__2__","gaps")
        ])