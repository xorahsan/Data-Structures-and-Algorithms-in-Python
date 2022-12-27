# Problem: Convert Infix expression to Prefix

import stacks
Stack = stacks.Stack

def get_operator_priority(op):
    priorities = {
        "^":3,
        "*":2,
        "/":2,
        "+":1,
        "-":1 
    }
    return priorities[op]

def main():
    _expression,expression, final_expression = "(A-B/C)*(A/K-L)","",""
    _expression = _expression[::-1]
    for i in _expression:
        if i == "(":
            expression+=")"
        elif i == ")":
            expression +="("
        else:
            expression+=i
    
    st = Stack()
    for i in expression:
        if i == "(":
            st.push(i)
        elif i == ")":
            while st.top() != "(":
                final_expression+= st.pop()
            st.pop()
        elif i in ("+","-","/","*","^"):
            if not st.isEmpty():
                top_item = st.top()
                if top_item != "(":
                    priority = get_operator_priority(i)
                    top_item_priority = -1 if top_item == "(" else get_operator_priority(top_item)
                
                    while not st.isEmpty() and top_item_priority >= priority:
                        if st.top() == "(": break
                        temp = st.pop()
                        top_item_priority = get_operator_priority(temp)
                        final_expression += temp
            st.push(i)
        else:
            final_expression+=i

    while not st.isEmpty():
        final_expression += st.pop()
    final_expression = final_expression[::-1]
    print(final_expression)

main()