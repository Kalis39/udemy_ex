import pandas
from test import add

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

is_on = True

while is_on:
    try:
        new_list = [new_dict[key] for key in input("Enter a word: ").upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet allowed.")
    else:
        print(new_list)
        is_on = False
