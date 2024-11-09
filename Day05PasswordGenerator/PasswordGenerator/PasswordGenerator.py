import random
from LettersNumbersSymbols import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_chosen_password = ""
random_chosen_password_list = []

for letter in range(0, nr_letters):
    random_chosen_letters = random.choice(letters)
    random_chosen_password += random_chosen_letters

for symbol in range(0, nr_symbols):
    random_chosen_symbols = random.choice(symbols)
    random_chosen_password += random_chosen_symbols

for number in range(0, nr_numbers):
    random_chosen_numbers = random.choice(numbers)
    random_chosen_password += random_chosen_numbers

random_chosen_password_list += random_chosen_password
# print(random_chosen_password_list)
random.shuffle(random_chosen_password_list)
# print(random_chosen_password_list)

final_password = ""
for key in random_chosen_password_list:
    final_password += key
print(f"Your Final Password: {final_password}")