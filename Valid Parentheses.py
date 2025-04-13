# Example 1: Input: s = "()" Output: true
# Example 2: Input: s = "()[]{}" Output: true
# Example 3: Input: s = "(]" Output: false
# Example 4: Input: s = "([])" Output: true


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    brackets = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for chart in s:
        if chart in brackets.values():  # открывающие скобки
            stack.append(chart)
        elif stack and stack[-1] == brackets[chart]:
            stack.pop()
        else:
            return False

    return not stack

    # return not stack


print(isValid("({[{[{}]}]})"))
