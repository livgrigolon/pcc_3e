# Lista de lugares para cada pessoa
favorite_places = {
    'livia': ['cafeteria'],
    'carol': ['academia'],
    'bruna': ['praia'],
    }

# Adicionando novos lugares via input
for i in range(2):
    name = input('Qual seu nome?\n').lower()
    favorite_place = input('Qual seu lugar favorito?\n')

    # Se a pessoa já existir, adiciona à lista
    if name in favorite_places:
        favorite_places[name].append(favorite_place)
    else:
        favorite_places[name] = [favorite_place]  # Cria nova lista

for name, places in favorite_places.items():
    print(f'\n{name.title()} gosta de:')
    for place in places:
        print(f"- {place.title()}") # Percorre cada item da lista separadamente