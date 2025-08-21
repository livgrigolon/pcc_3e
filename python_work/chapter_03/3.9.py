convidados = ['Orlando', 'Célia', 'Ricardo']

print(f'Olá, {convidados[0]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[1]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[2]}! Gostaria de te convidar para um jantar!')

print(f'Felizmente encontrei uma mesa maior, então teremos mais convidados!')

convidados.insert(0, 'Leoni')
convidados.insert(3, 'Lais')
convidados.append('Bernardo')
print(convidados)

print(f'Olá, {convidados[0]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[1]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[2]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[3]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[4]}! Gostaria de te convidar para um jantar!')
print(f'Olá, {convidados[5]}! Gostaria de te convidar para um jantar!')

print(f'Temos {len(convidados)} convidados para o jantar de hoje!')