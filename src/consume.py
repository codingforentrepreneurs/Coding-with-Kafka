import json
from kafka import KafkaConsumer

KAFKA_BROKER_URL="127.0.0.1:19092"
KAFKA_BROKER_URL2="127.0.0.1:19093"
KAFKA_BROKER_URL3="127.0.0.1:19094"
bootstrap_servers=[KAFKA_BROKER_URL, KAFKA_BROKER_URL2, KAFKA_BROKER_URL3]

KAFKA_TOPIC="hello-world"

consumer = KafkaConsumer(
    KAFKA_TOPIC, 
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='smallest' # from_beginning: true
)

for msg in consumer:
    raw_value = msg.value
    value_str = raw_value.decode("utf-8")
    try:
        data = json.loads(value_str)
    except json.decoder.JSONDecodeError:
        data = None
        print("invalid json")
    print(data, type(data), type(value_str))