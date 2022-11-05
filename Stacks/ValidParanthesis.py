def isValid(string):

    brackMapping = {
        "(":")",
        "{":"}",
        "[":"]"
    }

    openParams = set(["(", "{", "["])

    stack = []

    for s in string:
        if s in openParams:
            stack.append(s)
        elif stack and s == brackMapping[stack[-1]]: 
            stack.pop()
        else:
            return False
    
    return stack == []


if __name__ == "__main__":
    string = "]{}"
    print(isValid(string))