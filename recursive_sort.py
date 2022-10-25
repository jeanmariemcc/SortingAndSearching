# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Recursive Sort < O(n^2)
#
# NAME:         JeanMarie McCormack
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a less than O(n^2) sort function `recursive_sort`
# that takes an unordered array of numbers as a parameter
# and returns a sorted array using merge sort or quick
# sort using recursion, rather than loops.

# using recursive_sort to call and test the various sorts
#  submitting merge_sort for review
def recursive_sort(array):
    return merge_sort(array)
    #return recursive_sort2(array)


def merge_sort(array):
    # returns array with values of the input array sorted low to high
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    # create the left array tree and the right array tree until array lengths = 1
    #  then merge left and right (going up the tree as stack pops) 
    #  creating successively longer sorted arrays.
    #  Return one sorted array
    return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


def merge(left_array, right_array):
    # inputs: two arrays comprised of sorted numbers
    merged_array = []   # for output
    i = 0
    j = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1
        
    # if any elements remain in left_array or right_array, 
    #   append them to merged_array (only one will have "leftovers")
    while i < len(left_array):
        merged_array.append(left_array[i])
        i += 1
    while j < len(right_array):
        merged_array.append(right_array[j])
        j += 1
    return merged_array

    
    """
# This is not a merge sort, merely recursive binary
def recursive_sort3(array):
    if len(array) < 2:
        return array
    count = 0
    for i in range(len(array) -1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            count += 1
    if count == 0:  # if no swaps occured, we are done
        return array
    else:  
        return(recursive_sort3(array))
"""
# I found this on the internet - it works, but I need help unpacking it
# I think I just unpacked this, but wow.. I'd like to talk this through with someone.
#  What would the bigO be for this?
def recursive_sort2(array):
    if len(array) < 2:
        return array
    return (recursive_sort2([el for el in array[1:] if el <= array[0]]) + [array[0]] + recursive_sort2([el for el in array[1:] if el > array[0]]))

 
def main():
    
    arrays = [[445, 67, -2, 33, 0, -44, 134, -67], \
              [i for i in range(10)], \
              [i for i in range(10, -1, -1)], \
              [-1, 2, 1, 2, 1, -1, 1, 2, 2], \
              [2, 1], \
              [1, 2], \
              [2], \
              []]

    for a in arrays:
        print("Unordered:", a)
        print("Sorted:   ", recursive_sort(a))
        

main()
