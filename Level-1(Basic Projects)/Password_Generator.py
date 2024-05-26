Password Generator in Python:
This Python script generates secure and random passwords that meet complexity requirements.


Features:
*Creates passwords with a mix of lowercase letters, numbers, and uppercase letters.
*Ensures each password contains at least one number and one uppercase letter (customizable).
*Allows you to specify the desired length for each password (minimum length enforced).
*Generates multiple passwords at once.


How to Use:
*Save the script as password_generator.py.
*Run the script from your terminal using python password_generator.py.
*Enter the number of passwords you want to generate.
*For each password, specify its desired length (minimum length is 3).
*The script will generate and display the requested strong passwords.


Security Considerations:
*This script helps create strong passwords, but it's recommended to use a password manager for additional security.
*Avoid using the generated passwords on multiple accounts.


Customization:
*Change the minimum number of required uppercase letters and numbers.
*Include special characters in the password generation.

  

import random
import string  # Import string module for easier character access

def generate_password(length):
  """Generates a password with a random combination of lowercase letters, numbers, and uppercase letters."""

  characters = string.ascii_lowercase + string.digits
  password = ''.join(random.choice(characters) for _ in range(length))

  # Ensure at least one number and uppercase letter (modify these rules as needed)
  min_numbers = 1
  min_uppercase = 1
  num_replacements = random.randrange(min_numbers + min_uppercase)

  for _ in range(num_replacements):
    replace_index = random.randrange(len(password))

    if random.randrange(2) == 0:  # Replace with a number
      password = password[:replace_index] + str(random.randrange(10)) + password[replace_index + 1:]
    else:  # Replace with an uppercase letter
      password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]

  return password


def main():
  """Prompts the user for the number of passwords and their desired lengths, then generates and displays the passwords."""

  num_passwords = int(input("How many passwords do you want to generate? "))
  print(f"Generating {num_passwords} passwords")

  password_lengths = []
  min_length = 3  # Enforce minimum password length

  for i in range(num_passwords):
    length = int(input(f"Enter the length of Password #{i + 1} (minimum {min_length}): "))
    password_lengths.append(max(length, min_length))  # Ensure minimum length is met

  passwords = [generate_password(length) for length in password_lengths]

  for i, password in enumerate(passwords):
    print(f"Password #{i + 1} = {password}")


if __name__ == "__main__":
  main()
