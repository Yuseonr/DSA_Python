# 5 Aug 2025
# Exponential Time

#--------------------------------L1 : Polynomial vs Exponential --------------------------------

# Faster

#--------------------------------L2 : PlyTime = P--------------------------------

# More practical to solve with computers

#--------------------------------L3 : Reduction to P --------------------------------

def fib(n):
    if n <= 1:
        return n 
    grand_parent = 0
    parent = 1
    current = 0
    for i in range (n-1):
        current = grand_parent+parent
        grand_parent = parent
        parent = current
    return current

memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    else :
        result = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = result
    return result

#--------------------------------L4 : Order 2^N Exponential --------------------------------

def power_set(input_set):
    if not input_set :
        # print('Empty input')
        return [[]]
    else :
        all_subsets = [[]]
        for element in input_set :
            # print('subset_w_el')
            subsets_with_element = []
            for subset in all_subsets :
                # print('subset_in_all')
                new_subset = subset + [element] 
                subsets_with_element.append(new_subset)
            all_subsets.extend(subsets_with_element)
        return all_subsets

#--------------------------------L5 : Big O Categories Review--------------------------------

# O(n)

#--------------------------------L6 : Complexity Quiz --------------------------------

# O(1)

#--------------------------------L7 : Complexity Quiz --------------------------------

# O(n) salah
# O(log(n))

#--------------------------------L8 : Complexity Quiz --------------------------------

# O(2n)

#--------------------------------L9 : Complexity Quiz --------------------------------

# O(n)

#--------------------------------L10 : Exponen Growth Seq --------------------------------

def exponential_growth(n, factor, days):
    result =[n]
    for i in range(days):
        result.append(result[i]*factor)
    return result
