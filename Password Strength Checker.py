def password_strength_checker(password):

#Defines the minimum length a password should be
    min_length = 8

#Checks to see if password contains each of the following criteria
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in "!@#$%^&*()_-+=" for char in password)

#Determines the strength of the password using criteria such as length, and whether or not it contains uppercase, lowercase, digits and symbols
    strength_message = ""
    if len(password) < 8:
        strength_message = "Weak - Password must contain at least " + str(min_length) + " characters."
    elif not (has_uppercase and has_lowercase and has_digit and has_symbol):
        strength_message = "Medium - Password must contain an uppercase, lowercase, digits and symbols."
    else:
        strength_message = "Strong - Password meets minimum requirements."

#Stores a list of suggestions depending on what criteria the password meets
    suggestions = []
    if not has_uppercase:
        suggestions.append("Include uppercase letters (A-Z)")
    if not has_lowercase:
        suggestions.append("Include lowercase letters (a-z)")
    if not has_digit:
        suggestions.append("Include digits (0-9)")
    if not has_symbol:
        suggestions.append("Include symbols (!@#$%^&*()_-+=)")
    strength_message += "\nSuggestions to improve: " + ", ".join(suggestions)

    return strength_message

#Allows you to input the passsword to see the strength of the password and if any suggestions are to be made
password = input("Enter your password: ")
strength_message = password_strength_checker(password)
print(strength_message)