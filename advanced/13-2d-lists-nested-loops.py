# declare a 2d list
d2_list = [
    [1, 3, 5],
    [1, 3, 5, 6, 9],
    [1, 3, 5, 6]
]

print(d2_list)

# get a row by its index
print(d2_list[1])

# get an element by its index
print(d2_list[1][0])

# looping rows inside a 2d list
for row in d2_list:
    print(row)

# looping columns inside a 2d list
for r in d2_list:
    for c in r:
       print(c)
