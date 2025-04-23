from collections import deque

def is_palindrome(input_string):
    """
    Check if the input string is a palindrome using a deque.
    
    Args:
        input_string (str): The string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Preprocess: convert to lowercase and remove spaces
    processed_string = input_string.lower().replace(" ", "")
    
    # Create a deque from the processed string
    char_deque = deque(processed_string)
    
    # Compare characters from both ends
    while len(char_deque) > 1:
        # If characters from both ends don't match, it's not a palindrome
        if char_deque.popleft() != char_deque.pop():
            return False
    
    # If we've checked all characters and they all matched, it's a palindrome
    return True

# Test cases
if __name__ == "__main__":
    test_strings = [
        "madam",
        "No lemon no melon",
        "Not a palindrome",
        "race car",
    ]
    
    for string in test_strings:
        result = is_palindrome(string)
        print(f"'{string}' is a palindrome: {result}")
