convidados = ['Orlando', 'Célia', 'Ricardo']

print(f'Olá, {convidados[0]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[1]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[2]}! Gostaria de te convidar para um jantar!')

print(f'Infelizmente o/a {convidados[1]} não poderá comparecer.')

convidados.remove(convidados[1]) # Não precisa atribuir novamente à variável porque esses métodos já salvam na lista original
convidados.insert(1, 'Murilo')

print(f'Olá, {convidados[1]}! Gostaria de te convidar para um jantar!')

