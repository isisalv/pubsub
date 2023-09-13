import pika, sys, os

TIPOS_EVENTOS = ['workshop', 'palestra', 'amostra']

def envia_mensagem(mensagem:str, topico:str):
    # Estabelece conexão com o message broker
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declara tópico
    channel.exchange_declare(exchange='eventos', exchange_type='topic')

    # Envia mensagem
    channel.basic_publish(exchange='eventos',routing_key=topico, body=mensagem)

    # Fecha conexão
    connection.close()

# Enviar mensagens
while(True):
    publicador = sys.argv[1].upper() if len(sys.argv) > 1 else sys.argv[0]
    os.system('cls')
    print(f"\nPUBLICADOR - {publicador}")
    print("Eu envio divulgações de eventos!!\n\n")
    print("Selecione um tipo de evento: \n")
    for i, evento in enumerate(TIPOS_EVENTOS):
        print(f"{i+1} - {evento.capitalize()}")
    opt = int(input()) - 1
    mensagem = input("O nome do evento: ")
    envia_mensagem(mensagem, TIPOS_EVENTOS[opt])