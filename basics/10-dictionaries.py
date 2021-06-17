# declare a dictionary
dict = {}
print(dict)

# we can initialize it with any type of value
# keys must be unique
months = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    12: "hello",
    1: [True, "yes"]
}
print(months)

# get value by key
print(months["feb"])
print(months.get("feb"))
print(months.get(1))

# get default value if our values doesnt exist
print(months.get("apr", "this value not found"))

