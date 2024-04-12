import datetime
import json
import pathlib
import random
import uuid

from decouple import Config, RepositoryEnv
from kafka import KafkaProducer

# BASE_DIR should be ~/dev/coding-with-kafka/
BASE_DIR = pathlib.Path(__file__).resolve().parent

# ENV_PATH should be ~/dev/coding-with-kafka/.env
ENV_PATH = BASE_DIR.parent / ".env"

# this will load the environment variables
# from the .env filepath we specified
config = Config(RepositoryEnv(ENV_PATH))

# load the KAFKA_BOOTSTRAP_SERVERS environment variable
KAFKA_BOOTSTRAP_SERVERS = config(
    "KAFKA_BOOTSTRAP_SERVERS", cast=str, default="localhost:9092"
)

# We can even have the topic as an environment variable
KAFKA_TOPIC = config("KAFKA_TOPIC", cast=str, default="hello-world")


# split the KAFKA_BOOTSTRAP_SERVERS into a list
bootstrap_servers = []
if KAFKA_BOOTSTRAP_SERVERS is not None:
    bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS.split(",")

# create a KafkaProducer instance

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

for i in range(10):
    number = random.randint(1_000, 10_000) * i
    data = {
        "id": str(uuid.uuid4().hex),
        "timestamp": datetime.datetime.now().isoformat(),
        "message": f"Message {i}",
    }
    json_data = json.dumps(data)
    message = json_data.encode("utf-8")
    producer.send(KAFKA_TOPIC, message)
    print(f"Sent message {i}")
producer.flush()
