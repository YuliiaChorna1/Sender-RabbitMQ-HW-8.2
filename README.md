**Sender**

This project is a Python application designed to manage and send communications to contacts based on their preferred method (SMS or email).

**Features:**

* Stores contact information (full name, email, phone number, preferred contact method, birthday) in a MongoDB database.
* Generates fake contact data for testing purposes.
* Publishes messages to a RabbitMQ message broker based on the preferred contact method.
* Consumes messages from RabbitMQ queues for SMS and email, sends dummy messages (replace with actual implementation), and updates the `sent` flag for processed contacts.

**Project Structure:**

* `models.py`: Defines the `Contacts` model for storing contact information in MongoDB.
* `seed.py`: Generates and stores fake contact data in the database.
* `connect.py`: Establishes a connection to the MongoDB database using credentials stored in a configuration file (`config.ini`).
* `producer.py`: Publishes messages to RabbitMQ based on the preferred contact method.
* `consumer_sms.py`: Consumes messages from the SMS queue in RabbitMQ, simulates sending SMS messages, and updates the `sent` flag for the corresponding contact.
* `consumer_email.py`: Consumes messages from the email queue in RabbitMQ, simulates sending email messages, and updates the `sent` flag for the corresponding contact.

**Prerequisites:**

* Python 3.x
* MongoDB
* RabbitMQ
* Libraries:
    * `mongoengine` for MongoDB interaction
    * `faker` for generating fake data
    * `pika` for RabbitMQ communication

**Installation:**

1. Install the required libraries:

   ```bash
   pip install mongoengine faker pika
   ```

2. Configure your MongoDB connection details (username, password, database name) in the `config.ini` file.

**Usage:**

1. **Generate fake contacts (optional):**

   ```bash
   python seed.py
   ```

   This will create 5 fake contacts in the database.

2. **Run the producer:**

   ```bash
   python producer.py
   ```

   This will publish messages to RabbitMQ based on the stored contact information.

3. **Run the SMS and email consumers concurrently:**

   Open two separate terminal windows and run the following commands:

   **Terminal 1:**

   ```bash
   python consumer_sms.py
   ```

   **Terminal 2:**

   ```bash
   python consumer_email.py
   ```

   These will consume messages from the respective queues in RabbitMQ and simulate sending messages.

**Notes:**

* This project provides a basic framework for contact management and message sending. You'll need to replace the dummy message sending logic in the consumer modules with your actual implementation for SMS and email.
* Consider implementing error handling and logging for a more robust solution.
