version_list = input().split(".")

total_string = "".join(version_list)
total_numbers = int(total_string)

new_numbers = total_numbers + 1
new_string = str(new_numbers)

new_string = ".".join(new_string)

print(new_string)
