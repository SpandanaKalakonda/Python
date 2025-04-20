# We're trying to create a digital clone of DJ Khaled. No fancy AI or alorithms needed.

# Just take a number and add another one:



# More specifically, you are given an integer array digits, where each digits[i] is the ith digit of positive whole number. It is ordered from most significant to least significant digit.

# Return an array of digits of the number after adding another one to the input.

# Example #1 123+1 = 124
# Input: digits = [1, 2, 3]

# Output: [1, 2, 4]

# Example #2 69+1 =70
# Input: digits = [6, 9]

# Output: [7, 0]


def another_one(digits):
  i = len(digits) -1
  while i>=0 and digits[i] ==9:
    digits[i] = 0
    i-=1
    
  if i>=0:
    digits[i]+=1
    return digits
  else:
    return [1]+digits
