ingredientes = ""

while True:
    ingredientes = input('Qual ingrediente você gostaria na sua pizza? (Digite "quit" para sair) ')
    
    if ingredientes.lower() == 'quit':
          print("Encerrando o pedido de ingredientes.")
          break
    
    print(f'{ingredientes.title()} foi adicionado à sua pizza!')