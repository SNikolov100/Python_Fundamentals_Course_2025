class Zoo:
    _animals = 0

    def __init__(self, name_of_zoo):
        self.zoo_name = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo._animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f'Mammals in {self.zoo_name}: {", ".join(self.mammals)}\nTotal animals: {Zoo._animals}'
        elif species == "fish":
            return f'Fishes in {self.zoo_name}: {", ".join(self.fishes)}\nTotal animals: {Zoo._animals}'
        if species == "bird":
            return f'Birds in {self.zoo_name}: {", ".join(self.birds)}\nTotal animals: {Zoo._animals}'


zoo_name = input()
number_of_animals = int(input())
zoo = Zoo(zoo_name)

while True:
    data = input().split()
    if len(data) > 1:
        species_animal = data[0]
        name_animal = data[1]
        zoo.add_animal(species_animal, name_animal)
    else:
        species_animal = data[0]
        break

print(zoo.get_info(species_animal))
