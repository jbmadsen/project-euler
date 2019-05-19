#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-01
# Computation time: ?? seconds. (Solved intuitively) (answer: 73162890)
#

# Description:
# A common security method used for online banking is to ask the user
# for three random characters from a passcode.
# For example, if the passcode was 531278, they may asked for the 2nd, 3rd,
# and 5th characters; the expected reply would be: 317.
# 
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order,
# analyse the file so as to determine the shortest possible secret
# passcode of unknown length.

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

keylog = []

# Opens a text file and reads the first line, then closes the file again
logfile = open('079 - keylog.txt', 'r')
while True:
    try:
        keylog.append(eval(logfile.readline()))
    except Exception:
        break
logfile.close()

print (keylog)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
