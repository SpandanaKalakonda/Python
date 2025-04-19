# Given a number 
# n, write a formula that returns 
# In case you forgot the factorial formula, 
# n!=n∗(n−1)∗(n−2)∗.....2∗1.

# For example, 

# 5!=5∗4∗3∗2∗1=120 so we'd return 120.

# Assume is 
# n is a non-negative integer.

def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
