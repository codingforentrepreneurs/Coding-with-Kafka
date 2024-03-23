# Reference Commands


## Zookeeper in Docker Compose

__Enter Container__
```bash
docker compose exec -it zookeeper /bin/bash
```
> Assumes that `zookeeper` is the service/hostname in `compose.yaml`

__Zookeeper Shell__
```
/bin/zookeeper-shell localhost:2181
```

__Zookeeper Shell via Docker Compose__
```bash
docker compose exec -it zookeeper /bin/zookeeper-shell localhost:2181
```

__Zookeeper Instance, are you okay? (`ruok`)__

```bash
echo "ruok" | nc localhost 2181
```
or
```bash
echo "ruok" | nc zookeeper 2181
```

__Zookeeper stats (`stat`)__
```bash
echo "stat" | nc localhost 2181
```

__Zookeeper configuration (`conf`)__
```bash
echo "conf" | nc localhost 2181
```


## Kafka in Docker Compose

__Enter Container__
```bash
docker compose exec -it kafka-1 /bin/bash
```

__View Available Kafka CLIs__
```
ls /bin | grep "kafka"
```

Key ones:
- `kafka-topics`: to create/delete topics
- `kafka-console-producer`: to create messages for a topic
- `kafka-console-consumer`: to view messages for a topic


__Create a topic__
```bash
/bin/kafka-topics --bootstrap-server localhost:9092 --create --topic hello-world --partitions 4 --replication-factor 3
```

```python
# Understanding Partitions and Replication Factor
a = 'some_message'
b = 'some_other message'
c = 'yet another one'
d = 'new one'
e = 'newer one'
f = 'newest one'

my_topic = [a, b, c] 

my_topic = [
    [a, e], # kafka-1
    [b, d], # kafka-2
    [c, f] # kafka-3
] 

my_topic_copy = [
    [a, e], # kafka-2
    [b, d], # kafka-1
    [c, f] # kafka-3
] 

my_topic = [a, b,c,f,e,d] 
```


__Interactive shell for creating messages for an existing topic__

```bash
/bin/kafka-console-producer --bootstrap-server localhost:9092 --topic hello-world
```

__Listen for a topic's messages__
- Listen to messages for topic
```bash
/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic hello-world --from-beginning
```


__Create a topic and related messages__
```bash
/bin/kafka-topics --bootstrap-server=localhost:9092 --delete --if-exists --topic my-topic
```


## Kakfa on Virtual Machine

Assuming that kafka is avialable on `/opt/kafka`


__Start the default config__
```bash
/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
```

__Create a topic__
```bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic hello-world --partitions 1 --replication-factor 1
```

__Interactive shell for creating messages for an existing topic__

```bash
/opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic hello-world
```

__Listen for a topic's messages__
- Listen to messages for topic
```bash
/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic hello-world --from-beginning
```


__Delete a topic__
```bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server=localhost:9092 --delete --if-exists --topic hello-world
```

__List topics__
```bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list
```