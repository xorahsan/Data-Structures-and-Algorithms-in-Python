
# Problem: https://www.geeksforgeeks.org/find-index-closing-bracket-given-opening-bracket-expression/

import stacks
STACK = stacks.Stack

def main():
    
    s = input()
    pos = int(input())
    s = s[pos:]

    ind = 0
    st = STACK()
    for i in s:
        if i == "[":
            st.push(i)
        if i == "]":
            st.pop()
            if st.isEmpty():
                print(pos+ind)
                break
        ind+=1

main()