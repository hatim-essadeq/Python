# the input value must be an integer, otherwise throw an exception
try:
    value = int(input("Enter a number : "))
    print(value)
except:
    print("the value must be a number")

# error type
try:
    result = 10 / 0
    value = int(input("Enter another : "))
    print(value)
except ZeroDivisionError:
    print("Divided by 0 invalid")
except ValueError:
    print("the value must be a number")

# show error message
try:
    result = 10 / 0
    value = int(input("Enter another : "))
    print(value)
except ZeroDivisionError as zErr:
    print(zErr)
except ValueError as vErr:
    print(vErr)
