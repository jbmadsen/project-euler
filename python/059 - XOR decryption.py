#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-30
# Computation time: 0.718999862671 seconds.
#

# Description:
# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption key
# on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
# then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message,
# and the key is made up of random bytes. The user would keep the encrypted message
# and the encryption key in different locations, and without both "halves",
# it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is
# to use a password as a key. If the password is shorter than the message, which is likely,
# the key is repeated cyclically throughout the message.
# The balance for this method is using a sufficiently long password key for security,
# but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using cipher1.txt (right click and 'Save Link/Target As...'),
# a file containing the encrypted ASCII codes, and the knowledge that the plain text
# must contain common English words, decrypt the message and find the
# sum of the ASCII values in the original text.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# For int to ascii: ord('s') == 115
# For ascii to int: chr(115) == 's'
# XOR: 65 ^ 42 = 107, 107 ^ 42 == 65 (Not quite sure here)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#list_of_bad = ['*','/','_','"','#','�','%','&','=','?','+',':',';',
#               '{','}','[',']','.',',','^','~','<','>','\'','@','�','$','!']

# Imports the ascii from the text file
logfile = open('059 - cipher.txt', 'r')
tmp = eval(logfile.readline()) # A tuple
logfile.close()

found = False
key = []

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            tmp_list = []
            for x in range(0,50,3):
                tmp_list.append(chr(tmp[x] ^ ord(a)))
                tmp_list.append(chr(tmp[x+1] ^ ord(b)))
                tmp_list.append(chr(tmp[x+2] ^ ord(c)))

            for x in range(0,len(tmp_list)-3):
                tmp_str = ''
                tmp_str += tmp_list[x]
                tmp_str += tmp_list[x+1]
                tmp_str += tmp_list[x+2]
                tmp_str += tmp_list[x+3]
                if tmp_str == 'The ' or tmp_str == 'the ':
                    print ("Key Found!", "(", a,b,c, ")")
                    found = True
                    key.append(a)
                    key.append(b)
                    key.append(c)
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if found:
    tmp_list = []
    for n in range(0,len(tmp),3):
        if not n >= len(tmp):
            tmp_list.append(tmp[n] ^ ord(key[0]))
        if not n+1 >= len(tmp):
            tmp_list.append(tmp[n+1] ^ ord(key[1]))
        if not n+2 >= len(tmp):
            tmp_list.append(tmp[n+2] ^ ord(key[2]))

print (sum(tmp_list))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
