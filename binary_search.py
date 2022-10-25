# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Recursive Binary Search
#
# NAME:         JeanMarie McCormack
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a recursive function `search` that
# takes an ordered array of numbers as a parameter
# and a number to search for and returns the index
# of the number in the array using binary, or -1 otherwise. For
# full credit, the search should be implemented using
# recursion, rather than a loop.

def binary_search(array, num):
    return search(array, num, 0, len(array) - 1)

def search(array, num, left, right):
    middle = left + (right - left) // 2
    if left > right:
        return -1
    elif num < array[middle]:
        return search(array, num, left, middle -1)
    elif num > array[middle]:
        return search(array, num, middle + 1, right)
    else:
        # num has been found,
        # check for first occurrance of num 
        #  in the sub-set of the array in which it was found
        for i in range(left, middle + 1):
            #print(f'array[{i}] = {array[i]}')
            if array[i] == num:
               return i    


def main():
    """
    a = [i for i in range(-1, 10, 2)]
    print(a)
    for n in [1, 0, -1, 2, -2, 4, 5, 6, 7, -67, 134]:
        print("%5d index? %d" % (n, binary_search(a, n)) )
 
    """
        
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    print('expect 3, actual: ', binary_search(a, 2))

    #a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    print('expect 0, actual: ', binary_search(a, 1))    
    
    b = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3]
    print('expect 9, actual: ', binary_search(b, 3))    

        

main()
