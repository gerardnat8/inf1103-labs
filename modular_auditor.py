print("=============================")
print('New Smart Inventory Auditor')
print("=============================")

    
def get_valid_input():
    # Prompt once. Return an int, the string 'quit', or None if invalid.
    user_input = input("Enter stock quantity: ").strip()
 
    if user_input.lower() == "quit":
        return "quit"
 
    if not user_input.isdigit():
        if user_input.startswith('-') and user_input[1:].isdigit():
            print("Input Error: Negative numbers are not allowed.\n")
        else:
            print(f"Input Error: {user_input} is not a valid integer.\n")
        return None
 
    return int(user_input)


            

