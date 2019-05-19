#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-02
# Computation time: 14.3280000687 seconds.
#

# Description:
# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#
# Peter and Colin roll their dice and compare totals: the highest total wins.
# The result is a draw if the totals are equal.
#
# What is the probability that Pyramidal Pete beats Cubic Colin?
# Give your answer rounded to seven decimal places in the form 0.abcdefg

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Possible outcomes:
# Peter: 4 ** 9 = 262144
# Colin: 6 ** 6 = 46656

# First we need to find the likelyhood of every distinct outcome for both of them.
# Using nested loops
tmp_res_one = 0
tmp_res_two = 0
result = 0
peter = []
peter_above = []
peter_outcomes = 262144.0
colin = []
colin_outcomes = 46656.0

# Idea:
# Get a count of the probability for both peter and colin, as well as an "equal-or-above"
# for peter.. then calc for "above"-"normal", and the propability in 0.abcdefg if shown
for x in range(6,36+1):
    above_count = 0
    count = 0
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                for d in range(1,5):
                    for e in range(1,5):
                        for f in range(1,5):
                            for g in range(1,5):
                                for h in range(1,5):
                                    for i in range(1,5):
                                        if (a+b+c+d+e+f+g+h+i) == x:
                                            count += 1.0
                                        if (a+b+c+d+e+f+g+h+i) >= x:
                                            above_count += 1.0
    peter.append(count)
    peter_above.append(above_count)

for x in range(6,36+1):
    count = 0
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    for e in range(1,7):
                        for f in range(1,7):
                            if (a+b+c+d+e+f) == x:
                                count += 1.0
    colin.append(count)

for x in range(0,30+1):
    tmp_res_one += float((peter_above[x]/peter_outcomes)*(colin[x]/colin_outcomes))
for x in range(0,30+1):
    tmp_res_two += float((peter[x]/peter_outcomes)*(colin[x]/colin_outcomes))

print (tmp_res_one-tmp_res_two)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
