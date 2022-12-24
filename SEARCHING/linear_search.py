# linear search
# ===== Time Complexity =====
# Best: O(1)
# Average: O(n)
# Worst: O(n)

# using loops

def linear_search_using_loops(arr, value):
    flag, index = True, 0
    for item in arr:
        if item == value:
            flag = False
            return index
        index+=1
    if flag: return -1


# using recursion

def linear_search_using_recursion(arr, value, ind = 0):

    if ind == len(arr):
        return -1
    if arr[ind] == value:
        return ind
    return linear_search_using_recursion(arr, value, ind+1)
    

def main():

    arr = [1,1,1,2,2,2,2,3,4,55,5,5,6]
    result_loop = linear_search_using_loops(arr, 2)
    result_recursion = linear_search_using_recursion(arr, 6)
    print(result_loop, result_recursion)

main()