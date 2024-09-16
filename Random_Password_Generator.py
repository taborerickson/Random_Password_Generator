
# Importing libraries 
import random
import string

print("Random Password Generator")
print("At the prompt, enter the number of characters you want your random password to have.")

# Defining the function to generate the password 
def password_gen(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Defining the main function to run the generator
def main():
    try:
        length = int(input("Enter Number of Characters in Password: "))
        # Error handling for invalid entries 
        if length <= 0:
            print("Please enter a valid positive number of characters.")
            return
        password = password_gen(length)
        print("Randomly Generated Password: ", password)
    # Error handling for invalid entries
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Running the password generator 
if __name__ == "__main__":
    main()



