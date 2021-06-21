"""
 we have different modes:
 r : read
 w : write
 a : append (just for adding after last ligne)
 r+ : read plus (read and write in the same time)

_____________________________________________________________

                  | r   r+  w   w+  a   a+ |
__________________|________________________|
read              | *   *       *       *  |
write             |     *   *   *   *   *  |
create            |         *   *   *   *  |
truncate          |         *   *          |
position at start | *   *   *   *          |
position at end   |                 *   *  |
--------------------------------------------
_____________________________________________________________

for ??
    read         : r (initial position : Beginning)
    write        : truncate ??
                        - yes : w
                        - no  : a (initial position : End)
    read & write : truncate ??
                        - yes : w+
                        - no  : r+ (initial position : Beginning)
                                a+ (initial position : End)
"""

#################################################### reading files ####################################################
# path                 #mode
open('../resources/inputs.txt', "r")

# open the file
my_file = open('../resources/inputs.txt', "r")

# check if the file is available for reading or not
print(my_file.readable())

# read the file
print(my_file.read())

# read the file line by line
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

# read the file line by line inside a list
print(my_file.readlines())
print(my_file.readlines()[1])

# read the file using for loop
for i in my_file.readlines():
    print(i)

# close file
my_file.close()

#################################################### writing files ####################################################

# open the file in append mode
inputs_file = open("../resources/inputs.txt", "a")

# add data at the end of the file
inputs_file.write("\naddress:fes")

# add list of lines at the end of the file
inputs_file.writelines(["\nweight:90Kg", "\nheight:183cm"])

# close file
inputs_file.close()
