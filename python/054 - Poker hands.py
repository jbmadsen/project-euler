#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-30
# Computation time: 0.0629999637604 seconds.
#

# Description:
# In the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:
#
#    * High Card: Highest value card.                                   (highest card value)
#    * One Pair: Two cards of the same value.                           (100 + card value)
#    * Two Pairs: Two different pairs.                                  (200 + card value)
#    * Three of a Kind: Three cards of the same value.                  (300 + card value)
#    * Straight: All cards are consecutive values.                      (400 + card value)
#    * Flush: All cards of the same suit.                               (500 + highest card value)
#    * Full House: Three of a kind and a pair.                          (600 + highest card value)
#    * Four of a Kind: Four cards of the same value.                    (700 + card value)
#    * Straight Flush: All cards are consecutive values of same suit.   (900 + highest card value)
#    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.          (1000)
#
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins;
# for example, a pair of eights beats a pair of fives (see example 1 below).
# But if two ranks tie, for example, both players have a pair of queens,
# then highest cards in each hand are compared (see example 4 below);
# if the highest cards tie then the next highest cards are compared, and so on.
#
# Consider the following hands dealt to two players:
#   Player 1                Player 2
#   5H 5C 6S 7S KD          2C 3S 8S 8D TD
#   Pair of Fives           Pair of Eights
#
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Variables
poker_list = []
tmp = None

# Opens a text file and reads the first line, then closes the file again
logfile = open('054 - poker.txt', 'r')

while not tmp == '':
    tmp = logfile.readline()
    if not tmp == None:
        # Appends the hands as individual strings
        poker_list.append([tmp[0:14],tmp[15:-1]])
logfile.close()

def poker_win(alist):
    # Takes two hands (in a list) as inputs; ( e.g. ['QC KC 3S JC KD', '2C 8D AH QS TS'] )
    # Returns a winner (1 for hand 1, 2 for hand 2, 0 for a draw)
    def hand_score(hand):
        # Takes hand as a string
        hand_score = 0
        hand_card_types = [0,0,0,0] # Hearts, diamonds, clubs, spades
        hand_card_numbers = []

        # Test for clubs, spades, hearts and diamonds in a hand
        # And test for numbers
        for x in hand.replace(' ', ''):
            try:
                if x == 'H': hand_card_types[0] += 1
                elif x == 'D': hand_card_types[1] += 1
                elif x == 'C': hand_card_types[2] += 1
                elif x == 'S': hand_card_types[3] += 1
                elif x == 'T': hand_card_numbers.append(10)
                elif x == 'J': hand_card_numbers.append(11)
                elif x == 'Q': hand_card_numbers.append(12)
                elif x == 'K': hand_card_numbers.append(13)
                elif x == 'A': hand_card_numbers.append(14)
                else: hand_card_numbers.append(int(x))
            except Exception as e:
                print (x, e)
        # Give score based on card types (flush or no flush)
        for x in hand_card_types:
            if x == 5:
                hand_score += 500
        # Give score based on numbers (straight, pairs, full house, highest, etc.)
        hand_card_numbers.sort()
        if hand_card_numbers == [10,11,12,13,14] and hand_score == 500: # Royal flush
            hand_score += 500
        else: # The rest
            # Pairs the numbers
            tmp_list = []
            for a in hand_card_numbers:
                if not [hand_card_numbers.count(a),a] in tmp_list:
                    tmp_list.append([hand_card_numbers.count(a),a])
            #print tmp_list, len(tmp_list),
            # Set the scores accordingly to the pairs
            if len(tmp_list) == 5: # No pairs or straight
                if tmp_list[0][1]+4 == tmp_list[1][1]+3 == tmp_list[2][1]+2 == tmp_list[3][1]+1 == tmp_list[4][1]:
                    hand_score += tmp_list[-1][1]
                    hand_score += 400
                else:
                    hand_score += tmp_list[-1][1]
            elif len(tmp_list) == 4: # One pair
                for x in range(4):
                    if tmp_list[x][0] == 2:
                        hand_score += tmp_list[x][1]
                        hand_score += 100
            elif len(tmp_list) == 3: # Two pairs or three of a king
                tmp_number = 0
                for x in range(3):
                    if tmp_list[x][0] == 2:
                        if tmp_list[x][1] > tmp_number:
                            tmp_number = tmp_list[x][1]
                        hand_score += 100
                    elif tmp_list[x][0] == 3:
                        hand_score += tmp_list[x][1]
                        hand_score += 300
                hand_score += tmp_number
            elif len(tmp_list) == 2: # Full house or four of a kind
                for x in range(2):
                    if tmp_list[x][0] == 4:
                        hand_score += tmp_list[x][1]
                        hand_score += 700
                    elif tmp_list[x][0] == 3:
                        hand_score += tmp_list[x][1]
                        hand_score += 300
                    elif tmp_list[x][0] == 2:
                        hand_score += tmp_list[x][1]
                        hand_score += 300
            #print hand_score,
        return hand_score, tmp_list

    # Get the hand and score so far (flush, no flush, royal flush)
    one_score, _ = hand_score(alist[0])
    two_score, _ = hand_score(alist[1])

    if one_score > two_score:
        return 1
    elif one_score < two_score:
        return 2
    return 0

one = 0
# Test with the first element in the list
for x in range(len(poker_list)):
    #print poker_list[x],
    #print poker_win(poker_list[x])
    if poker_win(poker_list[x]) == 1:
        one += 1
print (one)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
