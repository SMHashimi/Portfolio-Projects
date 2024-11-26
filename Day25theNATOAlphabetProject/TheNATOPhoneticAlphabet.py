import pandas
nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# letter_and_code = {}
# for (index, row) in nato.iterrows():
#     letter = row.letter
#     # print(row.letter)
#     # print(row.code)
#     code = row.code
#     letter_and_code[letter] = code

nato_as_dict = {row.letter:row.code for (letter, row) in nato.iterrows()}
def phonetic():
    user_input = input("Please tell me your name? ").upper()
    try:
        words_list = [f"{letter} for {nato_as_dict[letter]}" for letter in user_input]
    except KeyError:
        print("Sorry, only letters are accepted.")
        phonetic()
    else:
        print(words_list)
phonetic()