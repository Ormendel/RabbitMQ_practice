import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = "localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print("[x] received %r" %body)


    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack = True)

    print(" [*] waiting for the messages. To exit press Ctrl-C")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

