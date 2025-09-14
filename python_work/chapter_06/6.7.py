dados_1 = {
    'first_name': 'Livia',
    'last_name': 'Grigolon',
    'age': 22,
    'city': 'Campinas'
    }

dados_2 = {
    'first_name': 'Isa',
    'last_name': 'Almeida',
    'age': 25,
    'city': 'Campinas'
    }

dados_3 = {
    'first_name': 'Carol',
    'last_name': 'Biage',
    'age': 26,
    'city': 'Campinas'
    }

people = [dados_1, dados_2, dados_3]

# for person in people:
#     print(f'{person.values()}')

for person in people:
    print(f"Nome: {person['first_name']} {person['last_name']}")
    print(f"Idade: {person['age']}")
    print(f"Cidade: {person['city']}\n")