"""
====================== insertion Sort =================
Best: O(n)
Average: O(n**2)
Worst: O(n**2)
"""

def insertion_sort(lst):
    for i in range(1,len(lst)):
        current = lst[i]
        j = i - 1
        while j >=0 and current < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = current

def main():
    temp = [12,3,9,0,-2,23,-32,-0,-1,1,9,3,7,4,0,1,2]
    insertion_sort(temp)
    print(temp)

main()