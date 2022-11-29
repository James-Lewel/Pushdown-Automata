from stack import Stack

# Initialize stack
stack = Stack()
stack.__init__()

# Brackets
openingBrackets = ['(', '{', '[']
closingBrackets = [')', '}', ']']

def start():
    userInput = input("\nEnter string : ")
    
    # Removes whitespace
    userInput = userInput.replace(' ', '')

    # Checks if condition matches
    isBalance = checkBalance(userInput)
    isBracket = checkBrackets(userInput)
    
    # Prints output
    if isBalance is True and isBracket is True:
        print("Brackets are balance!")
        
    elif isBalance is False and isBracket is True:
        print("Brackets are not balanced!")
        
    else:
        print("Input is not a bracket!")
        
# Checks if input is balance
def checkBalance(userInput):
    for bracket in userInput:
        if bracket in openingBrackets:
            stack.push(bracket)
        else:
            if stack.is_empty() is True:
                return False
            
            tempBracket = stack.pop()
            
            # Checks in bracket match with closing
            if tempBracket == '(':
                if bracket != ')':
                    return False
            elif tempBracket == '{':
                if bracket != '}':
                    return False
            elif tempBracket == '[':
                if bracket != ']':
                    return False
                
    return True if stack.is_empty() else False

# Checks if input is a bracket
def checkBrackets(userInput):
    for bracket in userInput:
        if bracket not in openingBrackets:
            if bracket not in closingBrackets:
                return False
        elif bracket not in closingBrackets:
            if bracket not in openingBrackets:
                return False
    return True