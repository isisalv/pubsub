import pika

TIPOS_EVENTOS = ['workshop', 'palestra', 'amostra']


def callback(ch, method, properties, body):
    topico = method.routing_key
    print(f"Um novo evento pra você!  {topico}: {body}")

def recebe_mensagens(topicos):
    # Conexão
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declara tópico
    channel.exchange_declare(exchange='logs', exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    for topico in topicos:
        channel.queue_bind(exchange='logs', queue=queue_name, routing_key=topico)

    print('Recebendo notificação de eventos =)')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

subscritos = []
continuar = True

# Selecionar tópicos pra inscrever
while(continuar):
    print("Selecione um tipo de evento para ser notificado: \n")
    for i, evento in enumerate(TIPOS_EVENTOS):
        print(f"{i+1} - {evento}")
    opt = int(input()) - 1
    topico = TIPOS_EVENTOS[opt]
    if topico not in subscritos:
        subscritos.append(TIPOS_EVENTOS[opt])
        opt = input("Deseja adicionar outro tipo de evento? (s/n)")
        if opt != 's':
            continuar = False
    else:
        print("Você já escolheu esse tipo de evento!")

# Inicia consumo
recebe_mensagens(subscritos)