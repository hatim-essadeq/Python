i = 0

while i < 10:
    print(i)
    i += 1
else:  # optional statement
    print("the loop has ended")

# continue (the loop will skip a statement)
j = 0
while j < 10:
    j += 1
    if j == 6:
        continue
    print(j)

# break (the loop will break looping)
k = 0
while k < 10:
    k += 1
    if k == 6:
        break
    print(k)
