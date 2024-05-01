secret_message = input()
secret_list = secret_message.split()

new_list = []
word_list = []
decipher_list = []

chr_code_string = ""
second_letter_index = 2
last_letter_index = -1

for word in secret_list:
    for letter in word:
        if letter.isnumeric():
            chr_code_string += letter

    chr_code = int(chr_code_string)
    chr_letter = chr(chr_code)
    word = word.replace(chr_code_string, chr_letter)
    new_list.append(word)
    chr_code_string = ""

for word in new_list:
    new_word = [letter for letter in word]
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    word = "".join(new_word)
    decipher_list.append(word)

decipher_message = " ".join(decipher_list)
print(decipher_message)
