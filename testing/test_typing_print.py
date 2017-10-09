from fill_in_the_gaps import typing_print

test_string = "Test"

print("")
typing_print(
    typing_string = test_string, 
    from_index = 0, 
    to_index = len(test_string), 
    step = 1, 
    delay = 0.1) 

print("")
typing_print(
    typing_string = test_string, 
    from_index = 0, 
    to_index = len(test_string), 
    step = 1, 
    delay = 0.1) 

print("")
typing_print(
    typing_string = test_string, 
    from_index = len(test_string), 
    to_index = 0, 
    step = -1, 
    delay = 0.1) 

print("")
typing_print("Default")
print("")

test_string = "This is a long one forward."

print("")
typing_print(
    typing_string = test_string, 
    from_index = 0, 
    to_index = len(test_string), 
    step = 2, 
    delay = 0.1) 


test_string = "This is a long one backward."

print("")
typing_print(
    typing_string = test_string, 
    from_index = len(test_string), 
    to_index = 0, 
    step = -2, 
    delay = 0.1) 
print("")
