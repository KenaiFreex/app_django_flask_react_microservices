import pika     # This module will help us to send the events to RabbitMQ
import json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://bcgiwipl:XUqhgdWxpCXg_eZM7Zvw3OB48bQmpg0V@toad.rmq.cloudamqp.com/bcgiwipl')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Receiving in admin...")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started Consuming...")

channel.start_consuming()

channel.close()