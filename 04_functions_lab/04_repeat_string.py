repeat_enter_string = lambda ent_string, counter: ent_string * counter


enter_string = input()
count = int(input())

result = repeat_enter_string(enter_string, count)
print(result)
