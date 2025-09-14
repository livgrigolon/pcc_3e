favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

pessoas = ['livia', 'maria', 'jen', 'phil']

for pessoa in pessoas:
    if pessoa in favorite_languages.keys():
        print(f'{pessoa.title()}, você já respondeu à pesquisa. Obrigada pela resposta!')
    else:
        print(f'Olá, {pessoa.title()}, gostaria de participar?')