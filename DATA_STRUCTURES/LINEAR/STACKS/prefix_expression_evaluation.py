# Problem: Evaluate Prefix Expression

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
    expression = list(map(convert, list("-+7*45+20")))
    expression = expression[::-1]
    operands = Stack()

    for i in expression:
        if isinstance(i, int):
            operands.push(i)
        else:
            a = operands.pop()
            b = operands.pop()
            temp = calc(b, a, i)
            operands.push(temp)
    
    print(operands.top())

main()