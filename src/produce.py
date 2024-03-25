import json
from kafka import KafkaProducer
import random

# KAFKA_BROKER_URL="127.0.0.1:19092"
# KAFKA_BROKER_URL2="127.0.0.1:19093"
# KAFKA_BROKER_URL3="127.0.0.1:19094"
# bootstrap_servers=[KAFKA_BROKER_URL, KAFKA_BROKER_URL2, KAFKA_BROKER_URL3]

KAFKA_BROKER_URL="172.234.228.67:19092"
bootstrap_servers=[KAFKA_BROKER_URL]

KAFKA_TOPIC="hello-world"

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

data = {
    "hello": "world"
}
data_json_str = json.dumps(data)
msg = data_json_str.encode('utf-8')

# send message
# print(msg, "not sent")

# future = producer.send(KAFKA_TOPIC, msg) # async
# result = future.get(timeout=60)
# print(result)

# producer.flush()

for _ in range(2):
    data = {'hello': f'world-{random.randint(10, 10_000)}'}
    data_json = json.dumps(data)
    data_ready = data_json.encode('utf-8')
    # data_ready = "hello world".encode('utf-8')
    producer.send(KAFKA_TOPIC, data_ready) #  partition=1)

producer.flush()