# declare a function
def say_hi():
    print("Hello world!")


# call the functtion
say_hi()


# passing parameters
def function_parameter(name, age):
    print("my name is " + name + ", my age is " + str(age))


function_parameter("Hatim", 24)


# we can return a value
def sum(num1, num2):
    return num1 + num2

print(sum(1,3))
