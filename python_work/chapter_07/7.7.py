# Loop infinito
while True:
    idade = int(input("Digite sua idade: "))
    
    if idade < 3:
        print("Ingresso gratuito!")
    elif 3 <= idade < 12:
        print("Ingresso: R$10,00")
    else:
        print("Ingresso: R$15,00")