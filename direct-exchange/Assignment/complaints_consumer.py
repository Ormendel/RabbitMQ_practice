import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='system_exchange', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='system_exchange', queue=queue_name, routing_key="Complaints")

print('[*] waiting for the messages')

def callback(ch, method, properties, body):
    print('[x] Complaint:::: %r' %body)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()




