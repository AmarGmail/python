def validate_login(username, password):

    # validate username
    if len(username) < 5:
        print("Error: Username must be at least 5 characters long.")
        return False

    # validate password
    if len(password) < 8:
        print("Error: Password must be at least 8 characters.")
        return False
    
    #Check if password string contains at least one digit
    for char in password:
        #print(char)
        if char.isdigit():
            return True # successfully completed validate_login

    print("Error: Password must contain at least one digit.")
    return False
    
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# call the validate_login function and check the result
if validate_login(username_input, password_input):
    print("Login successful")
    print("Return: True")
