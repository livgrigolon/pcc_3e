def show_messages(lista):
    for mensagem in lista:   # a função usa a lista que você passar
        print(mensagem)

messages = ['Oi!', 'Não posso falar agora.', 'Estou ocupada!']
show_messages(messages)

outra_lista = ['Bom dia!', 'Vamos estudar Python!']
show_messages(outra_lista)
