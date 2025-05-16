# reverse the string without useing the built in function

def reverse_string(s):
    reversed_str = " "  # Empty string to store result
    for char in s:
        reversed_str = char + reversed_str  # Add each c
        # haracter at the beginning
    return reversed_str

# Example usage
text = "hello"
print(reverse_string(text))  # Output: "olleh"



