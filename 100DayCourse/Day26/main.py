import pandas
 
nato_data_frame = pandas.read_csv("100DayCourse/Day26/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()

