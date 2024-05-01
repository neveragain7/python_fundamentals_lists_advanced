string_list = input().split(", ")

numbers_list = [int(symbol) for symbol in string_list]

positive_list = [str(number) for number in numbers_list if number >= 0]
negative_list = [str(number) for number in numbers_list if number < 0]
even_list = [str(number) for number in numbers_list if number % 2 == 0]
odd_list = [str(number) for number in numbers_list if not number % 2 == 0]

print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")
