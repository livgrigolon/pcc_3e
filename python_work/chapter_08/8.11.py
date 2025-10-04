messages = ['Oi!', 'Não posso falar agora.', 'Estou ocupada!']

# Lista que vai receber as mensagens enviadas
sent_messages = []

def send_messages(originais, enviadas):
    while originais:  # enquanto a lista original não estiver vazia
        message = originais.pop(0)  # pega a primeira mensagem
        print("Enviando:", message)
        enviadas.append(message)  # adiciona na lista de enviadas

send_messages(messages[:], sent_messages) # [:] Cópia da lista

print("Mensagens originais (depois do envio):", messages) # Não precisar printar com f-string
print("Mensagens enviadas:", sent_messages)
