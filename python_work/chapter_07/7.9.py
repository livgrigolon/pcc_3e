sandwich_orders = [
    'atum',
    'pastrami',
    'frango',
    'vegetariano',
    'bacon',
    'pastrami',
    'truffle burger',
    'pastrami'
]

finished_sandwiches = []

while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        print(f'Estamos sem sanduíche de Pastrami')
        sandwich_orders.remove('pastrami')
    
    sandwich = sandwich_orders.pop(0)  # remove o primeiro sanduíche da lista
    print(f"Seu lanche de {sandwich} está pronto!")
    finished_sandwiches.append(sandwich)  # adiciona à lista de prontos

# exibe todos os sanduíches prontos
print("\nTodos os sanduíches foram preparados:")
for i, sandwich in enumerate(finished_sandwiches, start=1): # enumerate adiciona um índice a cada item de uma lista
    print(f"{i}. {sandwich}")