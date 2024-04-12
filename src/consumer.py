import json
import pathlib

from decouple import Config, RepositoryEnv
from kafka import KafkaConsumer

# BASE_DIR should be ~/dev/coding-with-kafka/
BASE_DIR = pathlib.Path(__file__).resolve().parent

# ENV_PATH should be ~/dev/coding-with-kafka/.env
ENV_PATH = BASE_DIR.parent / '.env'

# this will load the environment variables
# from the .env filepath we specified
config = Config(RepositoryEnv(ENV_PATH))


# We can even have the topic as an environment variable
KAFKA_TOPIC = config('KAFKA_TOPIC', cast=str, default='hello-world')

# load the KAFKA_BOOTSTRAP_SERVERS environment variable
KAFKA_BOOTSTRAP_SERVERS = config('KAFKA_BOOTSTRAP_SERVERS', cast=str, default='localhost:9092')

# split the KAFKA_BOOTSTRAP_SERVERS into a list
bootstrap_servers =[]
if KAFKA_BOOTSTRAP_SERVERS is not None:
    bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS.split(',')

# create a KafkaConsumer instance

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=bootstrap_servers)

# assume messages with be in JSON format
for message in consumer:
    try:
        message_bytes = message.value
        message_data = message_bytes.decode('utf-8')
        data = json.loads(message_data)
    except Exception as e:
        print(f"Error processing JSON message: {e}")
        continue
    print("Message received:")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()