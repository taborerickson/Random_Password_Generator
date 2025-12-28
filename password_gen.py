# Importing libraries 
import random
import string
import secrets 

# Adding characters to be excluded from generated passwords 
# for systems that may not allow certain special characters in passwords
excluded_characters = set("(){}[]|/\\`~-_") 
# Building filtered punctuation list 
allowed_punctuation = ''.join(char for char in string.punctuation if char not in excluded_characters) 
# Full allowed characters set 
allowed_characters = string.ascii_letters + string.digits + allowed_punctuation

# General password generator function 
def basic_password(length): 
    """ 
    Generates a password using random library. 
    Useful for non-critical application passwords. 
    """
    password = ''.join(random.choice(allowed_characters) for _ in range(length)) 
    return password 

# Adding functionality for secure password 
def secure_password(length): 
    """  
    Generates a password using secrets library. 
    Useful for sensitive applications requiring strong security. 
    """
    password = ''.join(secrets.choice(allowed_characters) for _ in range(length)) 
    return password 

def main(): 
    print("*** Random Password Generator ***") 
    length = int(input("Enter desired password length: ")) 
    security_level = input(
        "Is this password for a sensitive application/high-security use? (yes/no): "
    ).strip().lower() 
    # Providing different password security level based on user input 
    if security_level == "yes": 
        password = secure_password(length) 
        print("\nPassword Security Level: [SECURE]") 
    else: 
        password = basic_password(length) 
        print("\nPassword Security: [BASIC]") 
    print("Generated Password: ", password) 


# Running the password generator 
if __name__ == "__main__":
    main()

