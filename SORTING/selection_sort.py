"""
====================== selection Sort =================
Best: O(n**2)
Average: O(n**2)
Worst: O(n**2)
"""

def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]: lst[i], lst[j] = lst[j],lst[i]
        



def main():
    temp = [12,3,9,0,-2,23,-32,-0,-1,1,9,3,7,4,0,1,2]
    selection_sort(temp)
    print(temp)

main()