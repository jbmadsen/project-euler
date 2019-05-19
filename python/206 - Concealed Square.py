#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-27
# Computation time: 15.5780000687 seconds.
#

# Description:
# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each '_' is a single digit.

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# As the form ends on _0, we know the only number who squared ends on 0 must end on 0 itself,
# thus the number has the form 1_2_3_4_5_6_7_8_900 ( 10 * 10 = 100 )
# We can therefore forget 00 ( for now ) and write 1_2_3_4_5_6_7_8_9
# Now.. the only two integers that squared equals nine are 3 and 7,
# Thus, if our math.sqrt(1_2_3_4_5_6_7_8_9) != 3 or 7, move to next

# Start value will be lowest square, floored to 100's. Alternative is = 1000000000
start_value = int(math.sqrt(1020304050607080900)) - (int(math.sqrt(1020304050607080900)) % 100) 
end_value = math.ceil(math.sqrt(1929394959697989900) + 100)
solution = False

def toString(number):
    # Takes a number and returns the squared in the form 1_2_3_4_5_6_7_8_9_0
    tmp_str = str(number * number)
    return_str = ''
    for n in range(len(tmp_str)):
        if n % 2 == 0:
            return_str += tmp_str[n]
        else:
            return_str += '_'
    return return_str

def trueString(number):
    # Returns true if number is in form 1_2_3_4_5_6_7_8_9_0
    tmp_str = str(number * number)
    try:
        if tmp_str[0] == '1':
            if tmp_str[2] == '2':
                if tmp_str[4] == '3':
                    if tmp_str[6] == '4':
                        if tmp_str[8] == '5':
                            if tmp_str[10] == '6':
                                if tmp_str[12] == '7':
                                    if tmp_str[14] == '8':
                                        if tmp_str[16] == '9':
                                            if tmp_str[18] == '0':
                                                return True
    except:
        return False
    return False

def test(start, end, incr):
    for current in range(start, end, incr):
        #print current
        #if toString(current) == '1_2_3_4_5_6_7_8_9_0':
        #    solution = True
        #    print "Solution:", current
        #    break
        if trueString(current):
            print ("Solution:", current)
            break

test(start_value + 30, end_value, 100)
print ("Done with 30's")
test(start_value + 70, end_value, 100)
print ("Done with 70's")

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
