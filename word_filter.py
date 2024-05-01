text = input().split()

new_list = [word for word in text if len(word) % 2 == 0]

for word in new_list:
    print(word)
