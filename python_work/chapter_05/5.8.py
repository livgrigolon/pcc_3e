username = ['Livia G', 'Isabella J', 'Carol G', 'Pedro F', 'admin']

for user in username:
    if user == 'admin':
        print('Olá admin, gostaria de ver um relatório de status?')
    else:
        print(f'Olá {user}, obrigada por fazer login novamente!')

