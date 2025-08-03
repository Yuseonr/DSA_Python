# 2/Aug/2025
# Big-O Analysis

#--------------------------------L1 : Big O Notation--------------------------------

# O(n^2)

#--------------------------------L2 : O(n) --------------------------------

def find_max(nums):
    max = nums[0]
    for num in nums :
        if num>max:
            max = num
    return max


#--------------------------------L3 : O(n^2)--------------------------------

def does_name_exist(first_names, last_names, full_name):
    for fn in first_names :
        for ln in last_names:
            if f"{fn} {ln}" == full_name:
                return True
    return False

#--------------------------------L4 : N^2 Quiz --------------------------------

# O(n), O(n^2)

#--------------------------------L5 : N^2 Quiz --------------------------------

# print_names_one

#--------------------------------L6 : O(nm) --------------------------------

def get_avg_brand_followers(all_handles, brand_name):
    inf_fol = 0
    brand_fol = 0
    for handle in all_handles :
        inf_fol += 1
        for each in handle :
            if brand_name in each :
                brand_fol +=1
    return brand_fol/inf_fol



#--------------------------------L7 : Constants doesnt matter --------------------------------

# O(2^n)

#--------------------------------L8 : Constants doesnt matter --------------------------------

# O(log(n))

#--------------------------------L9 : Constants Quiz --------------------------------

# O(n) O(n)

#--------------------------------L10 : Constants Quiz --------------------------------

# double_sum

#--------------------------------L11 : Order 1 --------------------------------

def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        return names_dict[first_name]
    return None

#--------------------------------L12 : Order Log N --------------------------------

def binary_search(target, arr):
    low = 0
    high = len(arr)-1
    while low <= high :
        med = (low + high)//2
        if arr[med] == target:
            return True
        elif arr[med] < target:
            low = med+1
        else : high = med-1
    return False

#--------------------------------L13 : Name Count --------------------------------

def count_names(list_of_lists, target_name):
    count = 0
    for list_of_list in list_of_lists:
        for list in list_of_list:
            if target_name in list:
                count+=1
    return count
