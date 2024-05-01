sequence_of_strings = input().split(", ")
sequence_of_numbers = [int(string) for string in sequence_of_strings]

max_number = max(sequence_of_numbers)
boundary = 10
new_list = []

while len(sequence_of_numbers) > 0:
    for index in range(len(sequence_of_numbers) - 1, -1, -1):
        number = sequence_of_numbers[index]
        if number <= boundary:
            new_list.append(number)
            sequence_of_numbers.remove(number)
    print(f"Group of {boundary}'s: {new_list[::-1]}")

    new_list = []
    boundary += 10
