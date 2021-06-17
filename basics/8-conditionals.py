is_hungry = True
wants_to_est = False

# we have two types of syntax
if (is_hungry):  # 1
    print("true")

if (is_hungry == True):  # 2
    print("true")

# using else
if (is_hungry):
    print("true")
else:
    print("false")

# or statements
if is_hungry or wants_to_est:
    print("or statements")

# and statements
if is_hungry and wants_to_est:
    print("and statements")

# else if
if is_hungry:
    print("is_hungry")
elif wants_to_est:
    print("wants_to_est")
else:
    print("do what you want")

# not (!)
if not is_hungry:
    print("is not hungry")
