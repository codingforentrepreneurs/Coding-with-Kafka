import json
from aiokafka import AIOKafkaProducer
import asyncio

KAFKA_BROKER_URL="127.0.0.1:19092"
KAFKA_TOPIC="hello-world"


async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL)
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    data = {'hello': 'aworld'}
    data_json = json.dumps(data)
    data_ready = data_json.encode('utf-8')
    try:
        # Produce message
        await producer.send_and_wait(KAFKA_TOPIC, data_ready)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

asyncio.run(send_one())