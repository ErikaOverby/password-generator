import random
import string

# Function to generate random password
def generate_password(nr_letters, nr_symbols, nr_numbers):
    # Lists for letters, symbols, and numbers
    letters = string.ascii_letters
    symbols = string.punctuation
    numbers = string.digits
    
    password_list = []
    
    # Add random letters
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    
    # Add random symbols
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))
    
    # Add random numbers
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Shuffle the password list to ensure randomness
    random.shuffle(password_list)
    
    # Join the list to form the final password
    password = ''.join(password_list)
    
    return password

# Input values for password generation
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))

# Generate the password
generated_password = generate_password(nr_letters, nr_symbols, nr_numbers)

# Display the result
print(f"Your password is: {generated_password}")
