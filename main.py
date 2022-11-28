import palindrome as palindrome
import brackets as brackets
import re

def main():
    userInput = input("1 - Palindrome\n"
                      "2 - Brackets\n"
                      "Enter : ")
    
    if userInput == "1":
        palindrome.start()
    elif userInput == "2":
        brackets.start()
    
    
if __name__ == "__main__":
    main()