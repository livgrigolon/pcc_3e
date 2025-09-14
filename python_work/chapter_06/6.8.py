cachorro = {
    'cachorro': 'jorge'
    }

gato = {
    'gato': 'isa'
    }

calopsita = {
    'calopsita': 'livia'
    }

pets = [cachorro, gato, calopsita]

for pet in pets:
    for animal, dono in pet.items(): # desempacotamento
        print(f"Animal: {animal.title()}")
        print(f"Dono: {dono.title()}")
