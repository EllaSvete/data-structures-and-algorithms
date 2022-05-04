def multi_bracket_validation(input_str):
    stack = []

    for paren in input_str:
        if paren == '(' or paren == '[' or paren == '{':
            stack.append(paren)
        else:
            if not stack:
                return False
            else:
                top = stack[-1]
                if paren == ')' and top == '(' or paren == ']' and top == '[' or paren == '}' and top == '{':
                    stack.pop()

    if not stack:
        return True
    else:
        return False


