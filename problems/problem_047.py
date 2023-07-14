# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False
    for character in password:
        if character.isalpha():
            if character.isupper():
                has_uppercase = True
            else:
                has_lowercase = True
        elif character.isdigit():
            has_digit = True
        elif character == "$" or character == "!" or character == "@":
            has_special_char = True
    return 6<=len(password)<=12 and has_digit and has_lowercase and has_uppercase and has_special_char


print(check_password("Helloworld!"))
