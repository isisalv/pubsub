import pika

TIPOS_EVENTOS = ['workshop', 'palestra', 'amostra']

def envia_mensagem(mensagem, topico):
    # Conexão
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declara tópico
    channel.exchange_declare(exchange='logs', exchange_type='topic')

    # Envia mensagem
    channel.basic_publish(exchange='logs',routing_key=topico, body=mensagem)
    print(f"Mensagem enviada - {topico}: {mensagem}")

    # Fecha conexão
    connection.close()

# Enviar mensagens
while(True):
    print("Selecione um tipo de evento: \n")
    for i, evento in enumerate(TIPOS_EVENTOS):
        print(f"{i+1} - {evento}")
    opt = int(input()) - 1
    mensagem = input("O nome do evento: ")
    envia_mensagem(mensagem, TIPOS_EVENTOS[opt])