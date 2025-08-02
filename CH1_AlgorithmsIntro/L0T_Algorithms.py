# 2/Aug/2025
# Algorithms intro

#--------------------------------L1 : Welcome to Data Structures --------------------------------

# Memorizing all the data structures and algorithms in this course

#--------------------------------L2 : Find Minimum --------------------------------

def find_minimum(nums):
    bignum = float("inf")
    if not nums :
        return None
    for num in nums :
        if num < bignum:
            bignum = num
    return bignum

#--------------------------------L3 : What is an Algorithms? --------------------------------

# finite

#--------------------------------L4 : What is an Algorithms? --------------------------------

# Reverse a string

#--------------------------------L5 : Simple Algorithms --------------------------------

def sum(nums):
    if not nums :
        return 0
    else :
        total = 0
        for num in nums :
            total+=num
        return total

#--------------------------------L6 : Avarage --------------------------------

def average_followers(nums):
    if not nums : return None
    total = 0
    member = 0
    for num in nums :
        total += num
        member += 1
    return total/member

