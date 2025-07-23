import pika
import sys

# Create a connection, say CN
# Create a channel in CN, say CH
# Create an Exchange
# Publish the message
# Close the connection
# Automatically closes the channel


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange = 'br_exchange', exchange_type='fanout')

messages = {0: 'Amlah', 1: 'Kadabra', 2: 'Katbam', 3: 'Bombs'}
for i in range(4):
    message = "Alert!!! : " + messages.get(i)
    channel.basic_publish(exchange='br_exchange', routing_key='', body = message)
    print("[x] sent %r" %message)

channel.exchange_delete(exchange='br_exchange', if_unused=False)

connection.close()


# # Sending messages to a specific queue is possible, even with fanout exchange. NOT RECOMMENDED!
# import pika
#
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
#
# # Declare a fanout exchange
# channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')
#
# # Declare and bind the specific queue
# channel.queue_declare(queue='QueueD', durable=True)
# channel.queue_bind(exchange='br_exchange', queue='QueueD')
#
# # Send multiple messages
# messages = {0: 'Amlah', 1: 'Missile', 2: 'Katbam', 3: 'Bombs'}
# for i in range(4):
#     message = "Alert!!! : " + messages.get(i)
#     channel.basic_publish(exchange='br_exchange', routing_key='', body=message)
#     print("[x] sent %r" % message)
#
# connection.close()
