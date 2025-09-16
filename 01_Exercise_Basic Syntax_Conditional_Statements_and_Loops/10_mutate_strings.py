first_string = input()
second_string = input()
mix_word = ""

for index in range(len(first_string)):
    mix_word = second_string[:index+1]
    mix_word += first_string[index+1:]
    if second_string[index] == first_string[index]:
        continue
    print(mix_word)

