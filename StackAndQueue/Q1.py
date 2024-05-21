def isValidKong(s):
    stack = []

    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        elif i in [')', '}', ']']:
            stack.pop()

    if (len(stack) == 0):
        return True
    else:
        return False

def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack

s = '{(([]))[}'

print(isValid(s))