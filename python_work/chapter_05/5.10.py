current_users = ['Livia', 'Isabella', 'BIA', 'Carol', 'Pedro', 'admin']
new_users = ['Nicollas', 'Bia', 'Isabella', 'Lucas', 'Maria']

# lista com o método .lower(), ou a função map() com uma função lambda
current_users_lower = [x.lower() for x in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"O nome de usuário '{user}' já está sendo utilizado. Escolha outro!")
    else:
        print(f"O nome de usuário '{user}' está disponível!")
