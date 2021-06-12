# we can print a string like this
stringValue = "this a string"
print(stringValue)
print("- type : " + str(type(stringValue)))
print("_____________________________________________________________________")

# in case that we need to use an integer, we must casting it to string type string str()
string_int = "this is a string : "+str(2)
print(string_int)
print("- type : " + str(type(string_int)))
print("_____________________________________________________________________")

# we can concatenate multiples variables using ","
print(stringValue, 2,"hhh")
print("_____________________________________________________________________")

# integer type
intValue = 2
print(intValue)
print("- type : " + str(type(intValue)))
print("_____________________________________________________________________")

# float type
floatValue = 1.5
print(floatValue)
print("- type : " + str(type(floatValue)))
print("_____________________________________________________________________")

# boolean type
boolTrue = True
boolFalse = False
print(str(boolTrue) + " != " + str(boolFalse))
print("- type : " + str(type(boolTrue)))
print("_____________________________________________________________________")

# complex type
complexValue = 1+3j
print(complexValue)
print("- type : " + str(type(complexValue)))
