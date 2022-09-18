cities = {
    'Tirana': {
        'country': 'albania',
        'population': 1_233_000,
        'fun_fact': 'It is the capital city of Albania',
    },
    'Paris': {
        'country': 'france',
        'population': 20_000_000,
        'fun_fact': 'The eiffel tower is there',
    },
    'Toronto': {
        'country': 'Canada',
        'population': 70_000_000,
        'fun_fact': 'It is the capital city of Canada'
    }
}

for city, city_info in cities.items():
    print(city.title())
    
    country = city_info['country'].title()
    print(f"Country: {country}.")

    population = city_info['population']
    print(population)

    fun_fact = city_info['fun_fact']
    print(f"{fun_fact}\n")

