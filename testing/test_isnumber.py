from fill_in_the_gaps import isnumber

print("###################")
print("Testing")
print("###################")

print("Should be True")
print(isnumber(2))
print(isnumber(2.223))
print(isnumber("2"))
print(isnumber("2.23"))

print("Should be False")
print(isnumber("2.sdsd"))
print(isnumber("test"))
print(isnumber(None))