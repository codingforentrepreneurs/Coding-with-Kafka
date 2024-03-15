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
/bin/kafka-topics --bootstrap-server localhost:9092 --create --topic hello-world --partitions 1 --replication-factor 1
```

__Interactive shell for creating messages for an existing topic__

```bash
kafka-console-producer --bootstrap-server localhost:9092 --topic hello-world
```

__Listen for a topic's messages__
- Listen to messages for topic
```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic hello-world --from-beginning
```


__Create a topic and related messages__
```bash
/bin/kafka-topics --bootstrap-server=localhost:9092 --delete --if-exists --topic my-topic
```
