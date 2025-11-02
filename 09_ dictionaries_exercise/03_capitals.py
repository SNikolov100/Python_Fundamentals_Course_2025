country_names = input().split(", ")
capital_cities = input().split(", ")

# countries_capitals_dict = dict(zip(country_names, capital_cities))
countries_capitals_dict = dict((country_names[index], capital_cities[index]) for index in range(len(country_names)))


for country, capital in countries_capitals_dict.items():
    print(f"{country} -> {capital}")
