def is_consonant(char):
    return char.isalpha() and char not in 'aeiou'

def solve(s):
    highest_value = 0
    current_value = 0

    for char in s:
        if is_consonant(char):
            current_value += ord(char) - ord('a') + 1
        else:
            highest_value = max(highest_value, current_value)
            current_value = 0
    
    return max(highest_value, current_value)

# Testing
print(solve("zodiacs"))  
print(solve("strength"))  
