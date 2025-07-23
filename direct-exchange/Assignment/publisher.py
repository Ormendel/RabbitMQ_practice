import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange = 'logs_exchange', exchange_type='direct')

severity = ["Alerts", "Suggestions", "Complaints"]
messages = ["Alert: There is a fire at ... place",
            "Suggestion: The quality of street lights should be improved at ... place",
            "Complaint: The electricity is not operational at ... place"]

for i in range(10):
    randomNum = random.randint(0, len(severity)-1)
    # print(randomNum)
    message = messages[randomNum]
    rk = severity[randomNum]
    print(f"{randomNum} -> {rk}")
    channel.basic_publish(exchange='system_exchange', routing_key=rk, body=message)
    print("[x] sent %r" %message)

channel.exchange_delete(exchange='system_exchange', if_unused=False)

connection.close()





