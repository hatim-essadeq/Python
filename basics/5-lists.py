# declare a list
persons = []
print(persons)

# we can initialize it with any type of value
values = [1, "string", True, ["11", "computer"]]
print(values)

# get a value from the list by its index
print(values[1])

# get last value of the list
print(values[-1])

# get values from an index to another index
print(values[1:3])  # index 3 not included

# get values from an index to the last one
print(values[2:])

# change value of a list by its integer
values[1] = "hello world"
print(values)

print("#############################################################################################")

list1 = ["python", "javascript", "php"]
list2 = [10, 23, 55]

# show both of the lists
print(list1, list2)

# concatenate 2 lists
list1.extend(list2)
list1 += list2
print(list1)

# add an element after the last element
list1.append("typescript")
print(list1)

# add an element after a specific index
list1.insert(0, "first element")
print(list1)

# remove an element by its value
list1.remove("first element")
print(list1)

# clear a list
list2.clear()
print(list2)

# show/remove the last item
print(list1.pop())
print(list1)

# get index element by its value
print(list1.index("python"))

# get occurrence count
list2 = ["python", "javascript", "python", "php"]
print(list2.count("python"))

# sort list values
list1.sort()
print(list1)

# make cory of a list (by value - shallow copy)
copy_list = list1.copy()
list1.append("another value")
print(list1, copy_list)

# make cory of a list (by reference)
copy_ref_list = list1
list1.append("ref value")
print(list1, copy_ref_list)
