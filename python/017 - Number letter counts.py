#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-24
# Computation time: 0.0 seconds.
#

# Description:
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used? 

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']  # 1-9
words_big = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',           # 0-9
             'sixteen', 'seventeen', 'eighteen', 'nineteen']                        
words_more = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',      # 0-9
              'eighty', 'ninety']

# Support a maximum number of 1000
def length_of_word(x, debug = False):
    length = 0
    hundreds = x // 100
    tmp_mod = x % 100
    tmp_str = str(tmp_mod)
    word = ""

    if x % 1000 == 0:
        length += len('one')                        # 3
        length += len('thousand')                   # 3
        if debug:
            word += "one thousand"

    if hundreds > 0 and not x == 1000:
        length += len(words[x // 100])              # 36
        length += len('hundred')                    # 63
        if debug:
            word += (words[x // 100] + 'hundred')

    if x > 100 and x < 1000 and not x % 100 == 0:
        length += len('and')                        # 2673
        if debug:
            word += (' and ')

    if tmp_mod >= 20 and tmp_mod < 100:
        length += len(words_more[int(tmp_str[0])])  # ??
        length += len(words[int(tmp_str[1])])       # ??
        if debug:
            word += (words_more[int(tmp_str[0])] + words[int(tmp_str[1])])

    if tmp_mod >= 10 and tmp_mod < 20:
        length += len(words_big[int(tmp_str[1])])   # ??
        if debug:
            word += words_big[int(tmp_str[1])]

    if tmp_mod < 10:
        length += len(words[int(tmp_str[0])])       # ??
        if debug:
            word += words[int(tmp_str[0])]

    if debug:
        print (word)

    return length

length = 0

# Sum up length of words
for x in range(1, 1001):
    length += length_of_word(x, False)

# Debug
#print length_of_word(1, True)

print (length)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
