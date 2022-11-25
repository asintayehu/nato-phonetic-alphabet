import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    pass
    # Access key and value


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

npa = pandas.read_csv("nato_phonetic_alphabet.csv")
npa_dict = npa.to_dict()
npa_df = pandas.DataFrame(npa_dict)

# print(npa_df)

# TODO 1. Create a dictionary in this format:
code_dict = {row.letter: row.code for (index, row) in npa_df.iterrows()}
# print(code_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input().upper()
name = list(name)
code_name = [code_dict[letter] for letter in name if letter in code_dict.keys()]
print(code_name)
