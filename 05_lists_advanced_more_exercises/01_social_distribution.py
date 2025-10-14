population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
need_money = 0
take_money = 0
is_not_possible = False

for _ in range(len(population)):
    wealth_person = max(population)
    wealth_person_index = population.index(wealth_person)
    poor_person = min(population)
    poor_person_index = population.index(poor_person)

    if poor_person < minimum_wealth:
        add_money_to_poor = minimum_wealth - poor_person
        population[poor_person_index] = add_money_to_poor + poor_person

        if wealth_person - add_money_to_poor >= minimum_wealth:
            wealth_person -= add_money_to_poor
            population[wealth_person_index] = wealth_person
        else:
            is_not_possible = True
            break

if is_not_possible:
    print("No equal distribution possible")
else:
    print(population)
