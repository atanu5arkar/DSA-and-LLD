"""
Why Stack?

The order in which the nested sequence of brackets are to be considered is same as that of popping
each bracket off of a stack.
"""


def valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for b in s:
        if not len(stack):
            stack.append(b)
        else:
            top = stack[-1]
            if b == pairs.get(top):
                stack.pop()
            else:
                stack.append(b)

    if len(stack): return False
    return True


print(valid_parentheses("([{}])"))
print(valid_parentheses("[(])"))
