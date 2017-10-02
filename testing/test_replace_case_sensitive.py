from fill_in_the_gaps import replace_case_sensitive

print("###################")
print("Testing")
print("###################")

print(replace_case_sensitive(
    phrase="_ a test. And _ time small.",
    placeholder="_",
    replacement="this"))

print(replace_case_sensitive(
    phrase="_ a test! _ time in the beginning of the sentence. And _ not.",
    placeholder="_",
    replacement="this"))

print(replace_case_sensitive(
    phrase="_ a test!? _ time in the beginning of the sentence. And _ not.",
    placeholder="_",
    replacement="this"))

print(replace_case_sensitive(
    phrase="_ a test._ is messed up.",
    placeholder="_",
    replacement="this"))