
import pika
import time
import json
from datetime import datetime
import connect
from models import Contacts


credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
)

channel = connection.channel()

channel.exchange_declare(exchange='message_operator', exchange_type='topic')

channel.queue_declare(queue='sms', durable=True)
channel.queue_bind(exchange='message_operator', queue='sms', routing_key="message.sms")

channel.queue_declare(queue='email', durable=True)
channel.queue_bind(exchange='message_operator', queue='email', routing_key="message.email")



def main():
    for contact in Contacts.objects():
        if contact.preferable == "sms":
            routing_key = "message.sms"
            method = "phone"
            contact_info = contact.phone
        else:
            routing_key = "message.email"
            method = "email"
            contact_info = contact.email
        
        message = {
            "object_id": str(contact.id),
            method: contact_info,
            "date": datetime.now().isoformat()
        }

        channel.basic_publish(
            exchange="message_operator",
            routing_key=routing_key,
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )

        print(" [x] Sent %r" % message)

        time.sleep(1)

    connection.close()


if __name__ == '__main__':
    main()
