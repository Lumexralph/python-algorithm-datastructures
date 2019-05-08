"""There are 90 cards with all two-digit numbers on them:
10,11,12,...,19,20,21,...,90,91,...,99.10,11,12,...,19,20,21,...,90,91,...,99.
A player takes some of these cards. For each card taken she gets $1. However,
if the player takes two cards that add up to 100 (say, 23 and 77), at the same time,
she loses all the money. How much could she get? (In mathematical language:
what is the maximum number of elements in a subset of \{11,12,...,99\}{11,12,...,99}
that does not contain any two numbers xx and yy with x+y=100x+y=100?)
"""

# values or integer generator
def generate_integer(start, end):
  num = start
  while num <= end:
    yield num
    num += 1



