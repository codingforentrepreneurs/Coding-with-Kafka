import pathlib
from typing import Union
from contextlib import asynccontextmanager
import json

from aiokafka import AIOKafkaProducer
from fastapi import FastAPI
from decouple import Config, RepositoryEnv



BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
CLUSTER_ENV_PATH = BASE_DIR / "cluster.env"
config = Config(RepositoryEnv(str(CLUSTER_ENV_PATH)))

KAFKA_BROKER_1=config('KAFKA_BROKER_1', default=None)
KAFKA_BROKER_2 = config("KAFKA_BROKER_2", default=None)
KAFKA_BROKER_3 = config("KAFKA_BROKER_3", default=None)
KAFKA_BROKER_4 = config("KAFKA_BROKER_4", default=None)
KAFKA_BROKER_5 = config("KAFKA_BROKER_5", default=None)
bootstrap_servers = [KAFKA_BROKER_1, KAFKA_BROKER_2, KAFKA_BROKER_3, KAFKA_BROKER_4, KAFKA_BROKER_5]

workers = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    producer = AIOKafkaProducer(bootstrap_servers=bootstrap_servers)
    await producer.start()
    workers['producer'] = producer
    yield 
    try:
        await producer.stop()
    except:
        pass
    workers.clear()



app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root(order_id:str=None):
    print(order_id)
    event_data = {"type": "orders/start", "order_id": order_id}
    data = json.dumps(event_data).encode("utf-8")
    producer = workers.get("producer")
    if producer is not None:
        topic = "some_topic"
        await producer.send_and_wait(topic, data)
    return {"Hello": "World", "BASE_DIR": BASE_DIR}


@app.get("/order/{order_id}")
async def read_order(order_id:str=None):
    print(order_id)
    event_data = {"type": "orders/shipped", "order_id": order_id}
    data = json.dumps(event_data).encode("utf-8")
    producer = workers.get("producer")
    if producer is not None:
        topic = "order_update"
        await producer.send_and_wait(topic, data)
    return {"Hello": "World", "BASE_DIR": BASE_DIR}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/about")
async def read_about():
    return {"Hello": "World"}
