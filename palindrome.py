from stack import Stack

# Initialize stack
stack = Stack()
stack.__init__()

def start():
    userInput = input("\nEnter string : ")
    
    # Removes whitespace
    userInput = userInput.replace(' ', '')
    
    # Checks if condition matches
    isPalindrome = check(userInput)
    
    # Prints output
    if isPalindrome is True:
        print(userInput + " is a palindrome!")
    else:
        print(userInput + " is not a palindrome!")

# Checks if input is a palindrome
def check(userInput):
    length = len(userInput) 
    half = length / 2
    count = 0
    
    for character in userInput:
        # Pushes first half of user input
        if count < int(half):
            stack.push(character)
            count += 1
        # Checks if first half matches with second half
        else:
            # Ignores middle character
            if count is int(half) and length % 2 != 0:
                count += 1
                continue
            tempCharacter = stack.pop()
            
            if tempCharacter is character:
                continue
            else:
                return False
    return True