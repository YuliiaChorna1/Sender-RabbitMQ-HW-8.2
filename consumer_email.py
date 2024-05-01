import time
import pika
import json
import connect
from models import Contacts


def send_email(contact_info, message):
    print(f"Message '{message}' sent to {contact_info}")


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    message: dict = json.loads(body)
    time.sleep(1)
    send_email(message["email"], "Yorr dedivedi has stak, follow this link http://scam.com")
    contact = Contacts.objects(id=message["object_id"])
    contact.update(sent=True)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='email', durable=True)
    channel.basic_consume(queue='email', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
