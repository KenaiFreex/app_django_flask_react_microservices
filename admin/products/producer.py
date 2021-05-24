import pika     # This module will help us to send the events to RabbitMQ
import json

params = pika.URLParameters('amqps://bcgiwipl:XUqhgdWxpCXg_eZM7Zvw3OB48bQmpg0V@toad.rmq.cloudamqp.com/bcgiwipl')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
