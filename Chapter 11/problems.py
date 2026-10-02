# Solution 11.1

def city_country(city, country, population):
    pair = f"{city}: {country} Population: {population}"
    return pair.title()

city_country_pair = city_country("karachi","pakistan",100000)
print(city_country_pair)