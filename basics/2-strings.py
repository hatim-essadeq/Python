# normal string
print("this is a string for Hatim")

# line break
print("this is a string for\nHatim")

# tabulation
print("this is a string for\tHatim")

# concatenation
print("this is a string for " + "Hatim")

text = "This is a string for hatim"

# lower case
print(text.lower())

# upper case
print(text.upper())

# check if it's upper or not
print(text.isupper())

# check if it's lower or not
print(text.islower())

# we can use multiple calls for multiple functions of the same variable
print(text.lower().islower())
print(text.upper().isupper())

# get de length of the string
print(len(text))

# get a character by its index
print(text[0])

# get the index of a character(s)
print(text.index("ha"))

# replace a character(s) by another character(s)
print(text.replace("for", "to"))
