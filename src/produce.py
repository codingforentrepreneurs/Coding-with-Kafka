import json
from kafka import KafkaProducer

KAFKA_BROKER_URL="127.0.0.1:19092" # where to send?
KAFKA_TOPIC="hello-world"

producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER_URL])

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

for _ in range(100):
    data = {'hello': 'world'}
    data_json = json.dumps(data)
    data_ready = data_json.encode('utf-8')
    producer.send(KAFKA_TOPIC, data_ready)

producer.flush()