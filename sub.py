import pika, sys, os

TIPOS_EVENTOS = ['workshop', 'palestra', 'amostra']


def callback(ch, method, properties, body):
    topico = method.routing_key.capitalize()
    print(f"\nUm novo evento pra você!  {topico}: {body.decode()}")

def recebe_mensagens(topicos):
    # Conexão
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declara tópico
    channel.exchange_declare(exchange='eventos', exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    for topico in topicos:
        channel.queue_bind(exchange='eventos', queue=queue_name, routing_key=topico)

    print('\nRecebendo notificações de eventos =)')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

subscritos = []
continuar = True

# Selecionar tópicos pra inscrever
while(continuar):
    assintante = sys.argv[1].upper() if len(sys.argv) > 1 else sys.argv[0]
    os.system('cls')
    print(f"\nASSINANTE - {assintante}")
    print("Eu recebo divulgações de eventos!!\n\n")
    print("Selecione um tipo de evento para ser notificado: \n")
    for i, evento in enumerate(TIPOS_EVENTOS):
        print(f"{i+1} - {evento.capitalize()}")
    opt = int(input()) - 1
    topico = TIPOS_EVENTOS[opt]
    if topico not in subscritos:
        subscritos.append(TIPOS_EVENTOS[opt])
        opt = input("Deseja adicionar outro tipo de evento? (s/n) ")
        if opt != 's':
            continuar = False
            os.system('cls')
    else:
        print("Você já escolheu esse tipo de evento!")
        input()

# Inicia consumo de mensagens
recebe_mensagens(subscritos)