def isPalindrome(s: str) -> bool:
    # Convert to lowercase
    s = s.lower()
    
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer if current character is not alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move right pointer if current character is not alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters
        if s[left] != s[right]:
            return False
        
        # Move both pointers
        left += 1
        right -= 1
    
    return True

# Example usage:
if __name__ == "__main__":
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "0P",
        "ab2a"
    ]
    for text in test_strings:
        print(f"{text!r} -> {isPalindrome(text)}")
