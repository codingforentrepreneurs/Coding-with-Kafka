import json
from kafka import KafkaConsumer, TopicPartition
import pathlib
from decouple import Config, RepositoryEnv
# KAFKA_BROKER_URL="127.0.0.1:19092"
# KAFKA_BROKER_URL2="127.0.0.1:19093"
# KAFKA_BROKER_URL3="127.0.0.1:19094"
# bootstrap_servers=[KAFKA_BROKER_URL, KAFKA_BROKER_URL2, KAFKA_BROKER_URL3]

# KAFKA_BROKER_URL="172.234.228.67:19092"
# bootstrap_servers=[KAFKA_BROKER_URL]

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
CLUSTER_ENV_PATH = BASE_DIR / "cluster.env"
config = Config(RepositoryEnv(str(CLUSTER_ENV_PATH)))

KAFKA_BROKER_1=config('KAFKA_BROKER_1', default=None)
KAFKA_BROKER_2 = config("KAFKA_BROKER_2", default=None)
KAFKA_BROKER_3 = config("KAFKA_BROKER_3", default=None)
KAFKA_BROKER_4 = config("KAFKA_BROKER_4", default=None)
KAFKA_BROKER_5 = config("KAFKA_BROKER_5", default=None)
bootstrap_servers = [KAFKA_BROKER_1, KAFKA_BROKER_2, KAFKA_BROKER_3, KAFKA_BROKER_4, KAFKA_BROKER_5]



KAFKA_TOPIC="some_topic"

consumer = KafkaConsumer(
    KAFKA_TOPIC, "order_update", 'webapp_page_view',
    bootstrap_servers=bootstrap_servers,
    # auto_offset_reset='smallest' # from_beginning: true
)
# consumer.assign([TopicPartition(KAFKA_TOPIC, 1)])

for msg in consumer:
    raw_value = msg.value
    value_str = raw_value.decode("utf-8")
    try:
        data = json.loads(value_str)
    except json.decoder.JSONDecodeError:
        data = None
        print("invalid json")
    print(data, type(data), type(value_str))