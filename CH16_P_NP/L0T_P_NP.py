# 16 Aug 2025
# P VS NP

#--------------------------------L1 : NP --------------------------------

# Super Set

#--------------------------------L2 : NP --------------------------------

# Verified

#--------------------------------L3 : Traveling Salesman Problem --------------------------------

def tsp(cities, paths, dist):
    check_paths = permutations(cities)
    for path in check_paths :
        distance = 0
        for i in range(len(path)-1):
            city_from = path[i]
            city_to = path[i+1]
            distance += paths[city_from][city_to]
        if distance < dist :
            return True
    return False

# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res


# print(tsp([0, 1, 2, 3, 4, 5, 6],
#         [
#             [0, 75, 920, 870, 700, 338, 483],
#             [75, 0, 573, 103, 362, 444, 323],
#             [920, 573, 0, 625, 655, 934, 209],
#             [870, 103, 625, 0, 989, 565, 488],
#             [700, 362, 655, 989, 0, 453, 886],
#             [338, 444, 934, 565, 453, 0, 533],
#             [483, 323, 209, 488, 886, 533, 0],
#         ],
#         2989))

#--------------------------------L4 : Verify TSP--------------------------------

def verify_tsp(paths, dist, actual_path):
    distance = 0
    for i in range(len(actual_path)-1):
            city_from = actual_path[i]
            city_to = actual_path[i+1]
            distance += paths[city_from][city_to]
    if distance < dist :
        return True
    return False
        
#--------------------------------L5 : TSP Review --------------------------------

# O(n!), O(n)

#--------------------------------L6 : TSP Review --------------------------------

# NP

#--------------------------------L7 : NP Complete --------------------------------

# in polynomial time

#--------------------------------L8 : NP Complete --------------------------------

# NP-complete, P

#--------------------------------L9 : Verifying Solutions --------------------------------

def get_num_guesses(length):
    if length == 1 :
        return 26
    return 26**length + get_num_guesses(length-1)

def get_num_guesses(length):
    # Using geometric series formula: a * (r^n - 1) / (r - 1)
    # where a = 26 (first term), r = 26 (common ratio), n = password_length
    return 26 * (26**length - 1) // 25

#--------------------------------L10 : Does P equal to NP --------------------------------

# P = NP

#--------------------------------L11 : Does P equal to NP --------------------------------

# We don't know, but probably not

#--------------------------------L12 : The Negative case --------------------------------

# We don't know

#--------------------------------L13 : The Negative case --------------------------------

# =, !=

#--------------------------------L14 : NP Hard --------------------------------

# have reductions from all NP problems

#--------------------------------L15 : NP Hard --------------------------------

# NP-complete, NP-hard

#--------------------------------L16 : Prime Factorization --------------------------------

import math

def prime_factors(n):
    pf = []
    i = 3
    while n % 2 == 0 :
        n /= 2
        pf.append(int(2))
    while i <= math.sqrt(n) :
        if n%i == 0 :
            n /= i
            pf.append(int(i))
        else : i += 2
    if n > 1 :
        pf.append(int(n))
    return pf

#--------------------------------L17 : Prime Factorization review --------------------------------

# NP

#--------------------------------L18 : Prime Factorization review --------------------------------

# Yes

#--------------------------------L19 : Prime Factorization review --------------------------------

# O(sqrt(n)), O(sqrt(2^s))

#--------------------------------L20 : Subset Sum Problem --------------------------------

def subset_sum(nums, target):
    return find_subset_sum(nums,target,index=len(nums)-1)


def find_subset_sum(nums, target, index):
    if target == 0 :
        return True
    if index < 0 and target != 0 :
        return False
    if nums[index] > target :
        return find_subset_sum(nums,target,index-1) 
    result = find_subset_sum(nums,target,index-1)
    sec_result = find_subset_sum(nums,target - nums[index],index-1)
    return result or sec_result


