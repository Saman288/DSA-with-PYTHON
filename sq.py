# Program to print squares of all numbers present in a list

numbers = [3, 7, 9, 12, 11, 10]

# to store square of each num
sq = 0

for val in numbers:
    # calculating square of each number
    sq = val * val
    # displaying the squares
    print(sq)