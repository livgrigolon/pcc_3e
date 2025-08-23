cubos = [ cubo **3 for cubo in range(1, 11) ]
print(cubos)

print(f'Os três primeiros elementos da lista são {cubos[:3]}')
print(f'Os três elementos do meio da lista são {cubos[3:7]}')
print(f'Os três últimos elementos da lista são {cubos[-3:]}')