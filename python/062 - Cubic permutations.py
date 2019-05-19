#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2019-05-12
# Computation time: 7.573390960693359 seconds 
#

# Description:
# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# 
# Find the smallest cube for which exactly five permutations of its digits are cube.


# Imports
import itertools

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Intuition
# Generate a dictionary to store cubed numbers + count of permutations 
# Iterate up through the integers, and either add to the dict or increase the counter
# Break on a counter of five

table = []
done = False
i = 0


class Cube:
    original : int = 0
    ordered : str = ""
    count : int = 0

    def __init__(self, n):
        self.original = n ** 3
        self.ordered = ''.join(sorted(str(self.original)))
        self.count = 1


while not done:
    i += 1
    cube = Cube(i)
    exists = [element.ordered for element in table if element.ordered == cube.ordered]
    if any(exists):
        #print("Ordered elements found:", exists)
        table_element = next((e for e in table if e.ordered == exists[0]), None) 
        index = table.index(table_element)
        table[index].count += 1
        if table[index].count == 5:
            print("Success")
            print("Solution:", table[index].original)
            done = True
            break
    else:
        table.append(cube)
        #print("Added:", cube.original, cube.ordered, "Table length:", len(table))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
