cars = ""

# enquanto o usuário não digitar 'sair', continua perguntando
while cars.lower() != "sair":
    cars = input('Que tipo de carro você gostaria de alugar? (digite "sair" para encerrar): ')
    
    if cars.lower() != "sair":  # evita imprimir quando o usuário quiser sair
        print(f"Veja-mos se consigo encontrar um {cars.title()} para você!\n")