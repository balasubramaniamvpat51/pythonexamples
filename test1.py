# Example 1: Check if string is None (null)
test_str = None
if test_str is None:
  print("String is null")

# Example 2: Check if string is empty
test_str = ""
if not test_str:  # This checks for empty string
  print("String is empty")

# Example 4: Loop through strings and check each
test_strings = [None, "", "Hello", "World", None, ""]
for test_str in test_strings:
    if test_str is None:
        print("String is null")
    elif not test_str:
        print("String is empty") 
    else:
        print(f"String value is: {test_str}")
        test_str = "Hello"
if test_str is not None and test_str:
  print("String is neither null nor empty")