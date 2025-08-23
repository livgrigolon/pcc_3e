buffet = ('Strogonoff', 'Macarronada', 'Risoto', 'Pizza', 'Hamburguer')

print('O restaurante oferece no Buffet:')
for comida in buffet:
    print(comida)

# buffet.append('Costela') # AttributeError: 'tuple' object has no attribute 'append'

buffet = ('Rondelli', 'Macarronada', 'Risoto', 'Pizza', 'Nhoque')
print('Agora o restaurante oferece no Buffet:')
for comida in buffet:
    print(comida)
