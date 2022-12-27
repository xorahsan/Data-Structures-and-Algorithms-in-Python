"""
====================== Bubble Sort =================
Best: O(n**2)
Average: O(n**2)
Worst: O(n**2)
"""

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]: lst[j], lst[j+1] = lst[j+1], lst[j]
        



def main():
    temp = [12,3,9,0,-2,23,-32,-0,-1,1,9,3,7,4,0,1,2]
    bubble_sort(temp)
    print(temp)

main()