cities = {
    'rio de janeiro': {
        'country': 'Brasil',
        'population': 6748000,
        'fact': 'Famosa pelo Cristo Redentor e o Carnaval.'
    },
    'paris': {
        'country': 'França',
        'population': 2148000,
        'fact': 'Conhecida como a "Cidade da Luz".'
    },
    'tóquio': {
        'country': 'Japão',
        'population': 13960000,
        'fact': 'É a maior metrópole do mundo em população.'
    }
    }

for city, info in cities.items(): # info -> dicionário com informações da cidade
    print(f"Cidade: {city.title()}")
    print(f"País: {info['country']}") # acessa o valor da chave 'country' no dicionário interno
    print(f"População: {info['population']}")
    print(f"Fato curioso: {info['fact']}\n")
