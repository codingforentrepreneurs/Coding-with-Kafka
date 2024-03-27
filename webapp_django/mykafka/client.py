import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from django.conf import settings
from decouple import Config, RepositoryEnv

BASE_DIR = settings.BASE_DIR
REPO_DIR = BASE_DIR.parent
CLUSTER_ENV_PATH = REPO_DIR / "cluster.env"

config = Config(RepositoryEnv(str(CLUSTER_ENV_PATH)))

KAFKA_BROKER_1=config('KAFKA_BROKER_1', default=None)
KAFKA_BROKER_2 = config("KAFKA_BROKER_2", default=None)
KAFKA_BROKER_3 = config("KAFKA_BROKER_3", default=None)
KAFKA_BROKER_4 = config("KAFKA_BROKER_4", default=None)
KAFKA_BROKER_5 = config("KAFKA_BROKER_5", default=None)
bootstrap_servers = [KAFKA_BROKER_1, KAFKA_BROKER_2, KAFKA_BROKER_3, KAFKA_BROKER_4, KAFKA_BROKER_5]

def get_consumer(topics=["default"], from_beginning=False):
    kafka_config = {
        "bootstrap_servers": bootstrap_servers,
    }
    if from_beginning:
        kafka_config['auto_offset_reset'] = 'smallest'
    return KafkaConsumer(
        *topics,
        **kafka_config
    )


def get_producer():
    return KafkaProducer(bootstrap_servers=bootstrap_servers)

def send_topic_data(data:dict, topic:str="some_example"):
    producer = get_producer()
    data_json = json.dumps(data)
    data_ready = data_json.encode('utf-8')
    return producer.send(topic, data_ready)