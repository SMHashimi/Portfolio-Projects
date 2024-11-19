import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# letter_and_code = {}
# for (index, row) in nato.iterrows():
#     letter = row.letter
#     # print(row.letter)
#     # print(row.code)
#     code = row.code
#     letter_and_code[letter] = code

user_input = input("Please tell me your name? ").upper()
nato_as_dict = {row.letter:row.code for (letter, row) in nato.iterrows()}
words_list = [f"{letter} for {nato_as_dict[letter]}" for letter in user_input]
print(words_list)




