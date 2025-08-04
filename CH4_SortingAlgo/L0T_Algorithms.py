# 4/aug/2025
# Sorting Algorithms

#--------------------------------L1 : Sorting Algorithms --------------------------------

class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

# dont touch above this line

def vanity(influencer):
    return influencer.num_selfies + (influencer.num_bio_links * 5)

def vanity_sort(influencers):
    return sorted(influencers,key=lambda influencer : vanity(influencer))

#--------------------------------L2 : Bubble sort --------------------------------

def bubble_sort(nums):
    end = len(nums)
    swapping = True
    while swapping :
        swapping = False
        for i in range (1, end):
            if nums[i-1]>nums[i]:
                nums[i-1],nums[i] = nums[i],nums[i-1]
                swapping = True
        end -= 1
    return nums

#--------------------------------L3 : Bubble Sort Big O--------------------------------

# O(n^2)

#--------------------------------L4 : Bubble Sort Big O--------------------------------

# At best n, at worst n^2

#--------------------------------L5 : Why Bubble Sort --------------------------------

# Because I'm studying algorithms

#--------------------------------L6 : Merge Sort --------------------------------

def merge_sort(nums):
    if len(nums)<2:
        return nums
    one_side = nums[:len(nums)//2]
    second_side = nums[len(nums)//2:]
    return merge(merge_sort(one_side), merge_sort(second_side))

def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second) :
        if first[i] <= second[j] :
            final.append(first[i])
            i += 1
        else : 
            final.append(second[j])
            j += 1
        print(final)
    if i<j :
        final.extend(first[i:])
    else : 
        final.extend(second[j:])
    return final

#--------------------------------L7 : Merge Sort Big O--------------------------------

# O(n*log(n))

#--------------------------------L8 : Why Merge sort --------------------------------

# Need a fast sorting algorithm and memory isn't an issue

#--------------------------------L9 : why merge sort --------------------------------

# merge_sort

#--------------------------------L10 : Insertion sort --------------------------------

def insertion_sort(nums):
    for i in range (len(nums)):
        j = i
        while j>0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

#--------------------------------L11 : Insertion Sort Big O--------------------------------

# O(n^2)

#--------------------------------L12 : Insertion Sort Big O--------------------------------

# Insertion Sort Big O

#--------------------------------L13 : Why use Insertion Sort--------------------------------

# Yes, but only on very small inputs

#--------------------------------L14 : Why use Insertion Sort--------------------------------

# insertion sort, merge sort

#--------------------------------L15 : Quick Sort --------------------------------

def quick_sort(nums, low, high):
    if low < high :
        middle = partition(nums,low,high)
        quick_sort(nums, low, middle - 1) 
        quick_sort(nums,middle + 1,high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low,high):
        if nums[j]<pivot:
            i+=1
            nums[i],nums[j] = nums[j], nums[i]
    nums[i+1],nums[high] = nums[high],nums[i+1]
    return i+1

# --------------------------------L16 : Quick Sort Big O--------------------------------

# An already sorted list

# --------------------------------L17 : QS Worst Complexity--------------------------------

# O(n^2)

# --------------------------------L18 : Fixing Quick Sort --------------------------------

# Practically ensures a runtime of O(n*log(n))

# --------------------------------L19 : Fixing QUick Sort --------------------------------

# It doesn't require randomness and impurity

# --------------------------------L20 : Why use Quick Sort --------------------------------

# Merge sort

# --------------------------------L21 : Why QS --------------------------------

# Quick sort

# --------------------------------L22 : Selection Sort--------------------------------

def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i, len(nums)):
            if nums[j]<nums[smallest_idx]:
                smallest_idx = j
        nums[i],nums[smallest_idx] = nums[smallest_idx],nums[i]
    return nums

