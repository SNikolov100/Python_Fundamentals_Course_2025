number_of_electrons = int(input())
shell = 0
electron_in_shell_list = []

while True:
    shell += 1
    value_shell = 2 * shell ** 2
    fill_electrons_in_shell = number_of_electrons - value_shell
    if fill_electrons_in_shell >= 0:
        number_of_electrons -= value_shell
        electron_in_shell_list.append(value_shell)
        if number_of_electrons == 0:
            break
    else:
        electron_in_shell_list.append(number_of_electrons)
        break

print(electron_in_shell_list)


