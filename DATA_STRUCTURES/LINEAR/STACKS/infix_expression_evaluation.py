# Problem: Evaluate Infinix Expression

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

def convert(i):
    return int(i) if i.isdigit() else i

def calc(a,b,s):
    if s == "+":
        return b + a
    elif s == "-":
        return b - a
    elif s == "*":
        return b * a
    elif s == "/":
        return b / a
    else:
        return b ** a

def main():
    expression = list(map(convert, list("1-9^2+8-0+8/2-1*9^0-1-1*2^9/3*5+9/3")))

    operands, operators = Stack(), Stack()

    for i in expression:
        
        if i == "(":
            operators.push(i)
        elif i == ")":
            while operators.top() != "(":
                
                sign = operators.pop() 
                a,b = operands.pop(),operands.pop()
                temp = calc(a,b,sign)
                operands.push(temp)

            operators.pop()

        elif i in ("+","-","/","*","^"):
            
            if not operators.isEmpty():
                top_item = operators.top()
                if top_item != "(":
                    priority = get_operator_priority(i)
                    top_item_priority = -1 if top_item == "(" else get_operator_priority(top_item)
                    while not operators.isEmpty() and top_item_priority >= priority:
                        
                        if operators.top() == "(": break
                        sign = operators.pop() 
                        a,b = operands.pop(),operands.pop()
                        temp = calc(a,b,sign)
                        operands.push(temp)
                        if not operators.isEmpty() : top_item_priority = get_operator_priority(operators.top())
                        
            operators.push(i)
            
        else:
            operands.push(i)
        
        
        
    while not operators.isEmpty():
        sign = operators.pop() 
        a,b = operands.pop(),operands.pop()
        temp = calc(a,b,sign)
        operands.push(temp)

    print(operands.top())

main()