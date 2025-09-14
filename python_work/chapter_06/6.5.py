# items(), keys() and values()
rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'yangzi': 'china'
}

for rio, pais in rios.items():
    print(f'O rio {rio.title()} atravessa o {pais.title()}')

for rio in rios.keys():
    print(f'{rio.title()}')

for pais in rios.values():
    print(f'{pais.title()}')