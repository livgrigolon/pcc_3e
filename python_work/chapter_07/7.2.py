while True:
    lugares = int(input('Quantos lugares você precisa na mesa? (ou digite "0" para encerrar) '))

    if lugares == 0:
        print("Encerrando o sistema de reservas.")
        break
    
    elif lugares > 8:
        print(f"É necessário aguardar por uma mesa de {lugares} lugares")
    else:
        print(f"Sua mesa já está pronta!")