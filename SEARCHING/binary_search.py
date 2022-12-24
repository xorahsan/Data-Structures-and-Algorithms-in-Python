# Binary Search
# ===== Time Complexity =====
# Best: O(1)
# Average: O(log n)
# Worst: O(log n)
from math import ceil

# using loops

def binary_search_loops(arr,value):
    start, end, mid = 0, len(arr)-1 , len(arr)//2

    while True:
        if start == end and value != arr[mid]:
            return -1
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            end = mid-1
            mid = (start+end)//2
        else:
            start = mid+1
            mid = (start+end)//2

# using recursion

def binary_search_recursive(arr, value, start,end, mid):
    if start == end and arr[mid] != value:
        return -1
    if arr[mid] == value:
        return mid
    elif value < arr[mid]:
        mid_new = (mid-1+start)//2
        return binary_search_recursive(arr, value, 0, mid-1,mid_new)
    else:
        mid_new = (mid+1+end)//2
        return binary_search_recursive(arr, value, mid+1, end,mid_new)


def main():

    arr = [1,2,3,4,5,6,7] 
    result_loop = binary_search_loops(arr, 1)
    result_recursion = binary_search_recursive(arr, 7,0,len(arr)-1,len(arr)//2)
    print(result_loop, result_recursion)

main()

