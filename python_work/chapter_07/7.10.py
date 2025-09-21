destinos = []

print('Pesquisa: Férias dos sonhos!')
print('Digite "sair" a qualquer momento para encerrar a pesquisa.')

while True:
    lugar = input('Se pudesse visitar qualquer lugar do mundo, para onde iria? ')
    if lugar.lower() == 'sair':
        break

    destinos.append(lugar)
    print(f"{lugar.title()} foi adicionado à pesquisa!\n")

print("Resultados da Pesquisa:")
for i, lugar in enumerate(destinos, start=1):
    print(f"{i}. {lugar.title()}")