scores = []

# score of player number 0:
scores.append([12, 16, 11, 12])

# score of player no. 1:
scores.append([9])

# score of player no. 2:
scores.append([6, 9, 11, 14, 17, 15, 14, 20])

# The list 'scores' has 3 elements, each element corresponding to a player.
# The element no. g in the list scores[p] corresponds to the score obtained
# in game number g played by player number p. The length of the lists 
# scores[p] vaires and eqauls 4, 1, and 8 for p equal to 0, 1, and 2,
# respectively.

# In a program, we must use 2 nested loops, one for the elements in 'scores'
# and one for the elements in the sublists of 'scores'. In the program below,
# we traverse a nested list using integer indices for each index:

for p in range(len(scores)):
    for g in range(len(scores[p])):
        score = scores[p][g]
        print '%4d' % score,   # With the trailing comma after the print string, we avoid a newline so
    print                      # that the column values in the table (i.e., scores for one player) appear
                               # at the same line. The single 'print' command after the loop over 'g'adds
                               # a newline after each table row.
                             

# With the trailing comma after the 'print' string, we avoid a newline so that 
# the column values in the table (i.e., scores for one player) appear at the
# same line. The single 'print' command after the loop over g adds a newline 
# after each table row.


# OUTPUT:

# src/looplist>   12   16   11   12
#    9
#    6    9   11   14   17   15   14   20

# The alternative version where we use variables for iterating over the 
# elements in the 'scores' lists and its sublists looks like this: 

for player in scores:
    for game in player:
        print '%4d' % game,
    print

# OUTPUT

# 12   16   11   12
#   9
#   6    9   11   14   17   15   14   20
