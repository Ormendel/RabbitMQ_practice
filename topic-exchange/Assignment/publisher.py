import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='alert_exchange', exchange_type='topic')

category = ['Alert', 'Suggestion', 'Complaint']
priority = ['Low', 'Med', 'High']
messages = {
    "Alert": "There is a fire at ... place",
    "Suggestion": "The quality of street lights should be improved at ... place",
    "Complaint": "The electricity is not operational at ... place"
}

for i in range(10):
    randomCategory = random.choice(category)
    randomPriority = random.choice(priority)
    routing_key = f"{randomCategory}.{randomPriority}"
    message = f"{messages[randomCategory]} ::::: <Message>"

    channel.basic_publish(exchange='alert_exchange', routing_key=routing_key, body=message)
    print(f"[x] sent {routing_key}: {message}")

# Only delete the exchange for cleanup/testing. In production, keep it.
# channel.exchange_delete(exchange='alert_exchange', if_unused=False)

connection.close()
