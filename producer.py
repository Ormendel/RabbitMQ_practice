import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="hello")

# In case of empty exchange, the queue and routing key must contain the same value
channel.basic_publish(exchange="", routing_key="hello", body="hello_world message #1")
print("[x] Sent Hello World")

connection.close()
