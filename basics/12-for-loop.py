# looping inside a string
for l in "hatim":
    print(l)

# looping inside a list
values = ["python", 1, True, (1, 5), ["what", "hi"]]
for e in values:
    print(e)

# looping inside a range
for i in range(10):  # not including last element (10)
    print(i)

# looping inside a range from a specific first element
for i in range(5, 15):
    print(i)

# looping inside a list using range
for i in range(len(values)):
    print(values[i])

# for else
for e in values:
    if e == "hatim":
        print(e)
        break
else:  # when the loop ends
    print("not found")
