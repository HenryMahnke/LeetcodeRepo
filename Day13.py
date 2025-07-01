"""valid parenthesis"""


def isValid(s):
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        else:
            if len(stack):
                cur = stack.pop()
            else: 
                return False
            if i == ")":
                if cur == "(":
                    continue
                else:
                    return False
            if i == "}":
                if cur == "{":
                    continue
                else:
                    return False
            if i == "]":
                if cur == "[":
                    continue
                else:
                    return False
    if len(stack):
        return False
    return True


s = "]]"
print(isValid(s))
