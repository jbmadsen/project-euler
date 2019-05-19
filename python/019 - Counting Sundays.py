#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-24
# Computation time: 0.0150001049042 seconds.
#

# Description:
# You are given the following information,
# but you may prefer to do some research for yourself.
#
#    * 1 Jan 1900 was a Monday.
#    * Thirty days has September,
#      April, June and November.
#      All the rest have thirty-one,
#      Saving February alone,
#      Which has twenty-eight, rain or shine.
#      And on leap years, twenty-nine.
#    * A leap year occurs on any year evenly divisible by 4,
#      but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Weekdays
week_days = ['sunday', 'monday', 'tuesday', 'wedensday',       # 0-6
            'thursday', 'friday', 'saturday']
# Months
months = { 1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5 }

# Make use of : http://en.wikipedia.org/wiki/Calculating_the_day_of_the_week
# Calculating leap year is missing
def get_day(day, month, year):
    if not day > 0 and not day <= 31:
        return None
    if not month > 0 and not month <= 12:
        return None
    century = 2 * (3 - ((year / 100) % 4))                              # step 1
    last_digits = year % 100                                            # step 2
    last_digits_divided = math.floor(last_digits / 4)                   # step 3
    mon = months[month]                                                 # step 4
    tmp_n = century + last_digits + last_digits_divided + mon + day     # step 5

    leap_year = 0                                                       # Calc leap year
    if month <= 2:
        if year % 4 == 0:
            if not year % 100 == 0 or year % 400 == 0:
                leap_year = -1

    remainder = int((tmp_n + leap_year) % 7)                            # step 6
    week_day = week_days[remainder]                                     # step 7

    return week_day

# The actual puzzle
number_of_sundays = 0

for y in range(1901, 2001):
    for m in range(1, 13):
        #print 1, m, y, get_day(1, m, y)
        if get_day(1, m, y) == 'sunday':
            number_of_sundays += 1

print ("sunday", number_of_sundays)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
