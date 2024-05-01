first_sequence = input().split(", ")
second_sequence = input().split(", ")

new_list = []

for word_1 in first_sequence:
    for word_2 in second_sequence:
        if word_1 in word_2 and word_1 not in new_list:
            new_list.append(word_1)

print(new_list)
