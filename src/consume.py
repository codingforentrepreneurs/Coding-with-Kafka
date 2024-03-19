import json
from kafka import KafkaConsumer

KAFKA_BROKER_URL="127.0.0.1:19092" # where to send?
KAFKA_TOPIC="hello-world"

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_BROKER_URL])

for msg in consumer:
    raw_value = msg.value
    value_str = raw_value.decode("utf-8")
    try:
        data = json.loads(value_str)
    except json.decoder.JSONDecodeError:
        data = None
        print("invalid json")
    print(data, type(data), type(value_str))