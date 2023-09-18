# pubsub
Trabalho de Publish/Subscribe

Broker: RabbitMQ
Linguagem: Python 
Obs.: a conexão com o broker se dá através da biblioteca Pika.

Neste projeto há duas aplicações: o publicador de eventos acadêmicos e a aplicação que se subscreve aos eventos publicados.
A publicação é feita por meio de três tópicos: workshop, palestra e amostra.
O consumidor pode se inscrever em um ou mais tópicos. 
Após de terminar sua inscrição, ele passa a escutar por mensagens nos tópicos escolhidos, independente de quem está publicando no canal.
Para divulgar um evento, o publicador deve apenas informar o tópico e o nome do evento. Após a confirmação, a mensagem é enviada para o message broker.
