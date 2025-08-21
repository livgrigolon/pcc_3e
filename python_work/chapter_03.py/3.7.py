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

print(f'Infelizmente não foi possível encontrar uma mesa maior a tempo, então teremos apenas dois convidados.')

convidados_removidos = convidados.pop()
print(f'Olá, {convidados_removidos}! Lamento não poder te convidar para o jantar dessa vez!')
convidados_removidos = convidados.pop()
print(f'Olá, {convidados_removidos}! Lamento não poder te convidar para o jantar dessa vez!')
convidados_removidos = convidados.pop()
print(f'Olá, {convidados_removidos}! Lamento não poder te convidar para o jantar dessa vez!')
convidados_removidos = convidados.pop()
print(f'Olá, {convidados_removidos}! Lamento não poder te convidar para o jantar dessa vez!')

print(f'Olá, {convidados[0]}! Seu convite para o jantar ainda está de pé!')
print(f'Olá, {convidados[1]}! Seu convite para o jantar ainda está de pé!')

del convidados[0]
del convidados[0]
print(convidados)