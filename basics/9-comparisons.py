# greater/lower than
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(1, 5, 2))

# equal and not equal
def match_strings(str1, str2):
    if str1 == str2:  # equal | for not equal : (!=)
        print("the strings do match")
    else:
        print("the strings does not match")


match_strings("hatim", "hatim")
