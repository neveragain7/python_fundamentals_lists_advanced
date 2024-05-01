number_of_electrons = int(input())

shell_position = 0
shell_electrons = 0
new_list = []

while number_of_electrons > 0:
    shell_position += 1
    shell_electrons = 2 * shell_position ** 2
    if shell_electrons <= number_of_electrons:
        new_list.append(shell_electrons)
    else:
        new_list.append(number_of_electrons)
    number_of_electrons -= shell_electrons

print(new_list)
