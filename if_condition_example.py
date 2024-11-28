# Example of correct if condition syntax for checking if both a and b are 0

# Incorrect way (could lead to unexpected behavior):
a = 1
b = 0
if a and b == 0:    # This only checks if (a is truthy) AND (b equals 0)
    print("Wrong! This condition will be true when a is any non-zero number and b is 0")

# Correct way:
a = 1
b = 0
if a == 0 and b == 0:    # This correctly checks if both a and b equal 0
    print("Correct! This condition will only be true when both a AND b are 0")