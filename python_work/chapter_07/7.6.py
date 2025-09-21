# Loop infinito, interrompido com break
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

# Controlando o loop com a variável 'active'
# active = True

# while active:
#     idade = int(input("Digite sua idade (0 para sair): "))
    
#     if idade == 0:
#         print("Encerrando o sistema de ingressos.")
#         active = False  # altera a variável para parar o loop
#     elif idade < 3:
#         print("Ingresso gratuito!")
#     elif 3 <= idade < 12:
#         print("Ingresso: R$10,00")
#     else:
#         print("Ingresso: R$15,00")

# Loop baseado em condição
# idade = 0

# while idade != -1:  # enquanto a idade não for -1, o loop continua
#     idade = int(input("Digite sua idade (-1 para encerrar): "))
    
#     if idade == -1:
#         print("Encerrando o sistema de ingressos.")
#     elif idade < 3:
#         print("Ingresso gratuito!")
#     elif 3 <= idade < 12:
#         print("Ingresso: R$10,00")
#     else:
#         print("Ingresso: R$15,00")