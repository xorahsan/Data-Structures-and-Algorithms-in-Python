# Problem: Convert Infix expression to Postfix

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
    expression, final_expression = "A*(B+C)/D",""
    st = Stack()
    for i in expression:
        if i == "(":
            st.push(i)
        elif i == ")":
            while st.top() != "(":
                final_expression+= st.pop()
            st.pop()
        elif i in ("+","-","/","*","^"):
            if st.isEmpty():
                st.push(i)
            else:
                top_item = st.top()
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

    print(final_expression)

main()