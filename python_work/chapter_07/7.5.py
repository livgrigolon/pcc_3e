ingresso = ""

while True:
    entrada = input('Digite sua idade (ou "sair" para encerrar): ')
    
    if entrada.lower() == 'sair':
        print("Encerrando o sistema de ingressos.")
        break
    
    idade = int(entrada)

    if idade < 3:
        print('Seu ingresso é gratuito!')
    elif 3 <= idade < 12:
        print('O ingresso custa R$10,00')
    else:
        print('O ingresso custa R$15,00')