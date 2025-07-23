import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='alert_exchange', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Catch all high-priority complaints messages
channel.queue_bind(exchange='alert_exchange', queue=queue_name, routing_key="Complaint.High")

print('[*] Waiting for high-priority complaints messages...')

def callback(ch, method, properties, body):
    print(f'[x] Received ({method.routing_key}): {body.decode()}')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
