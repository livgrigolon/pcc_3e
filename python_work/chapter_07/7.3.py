while True:
    numero = input('Digite um número (ou "sair" para encerrar o programa): ')

    if numero.lower() == 'sair':
        print(f'Encerrando o programa...')
        break
    
    numero = int(numero)

    if numero % 10 == 0:
        print(f'O número {numero} é múltiplo de 10!')
    else:
        print(f'O número {numero} não é múltiplo de 10!')