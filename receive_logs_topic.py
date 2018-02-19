#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

f = open('receive.log', 'w')
f.write(' [*] Waiting for logs\n')
f.close()

def callback(ch, method, properties, body):
    f = open('receive.log', 'a')
    f.write(" [x] %r:%r\n" % (method.routing_key, body))
    f.close()

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
