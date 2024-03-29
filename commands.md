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


## Zookeeper on Virtual Machine

Assuming that kafka is avialable on `/opt/kafka`, you can use the following:


__Start with the default config__
```bash
/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
```

__Start with the custom config__

```bash
/opt/kafka/bin/zookeeper-server-start.sh /data/my-config/zookeeper.properties
```
`/data/my-config/zookeeper.properties` is essentially the same as the default config with some minor changes (including the Zookeeper servers in the quorom).

__Stop with the default config__
```bash
/opt/kafka/bin/zookeeper-server-stop.sh
```

__Zookeeper Shell when Zookeeper is running/available__
```bash
/opt/kafka/bin/zookeeper-shell.sh localhost:2181
```


## Kakfa on Virtual Machine

Assuming that kafka is avialable on `/opt/kafka`


__Start the default config__
```bash
/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
```

__Start the custom config__
```bash
/opt/kafka/bin/kafka-server-start.sh /data/my-config/server.properties
```

__Create a topic__
```bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server kafka1:9092 --create --topic hello-world --partitions 1 --replication-factor 1
```

__Interactive shell for creating messages for an existing topic__

```bash
/opt/kafka/bin/kafka-console-producer.sh --bootstrap-server kafka1:9092 --topic hello-world
```

__Listen for a topic's messages__
- Listen to messages for topic
```bash
/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka1:9092 --topic hello-world --from-beginning
```


__Delete a topic__
```bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server=kafka1:9092 --delete --if-exists --topic hello-world
```

__List topics__
```bash
/opt/kafka/bin/kafka-topics.sh --bootstrap-server=kafka1:9092 --list
```


## Systemd Commands

__Create a new service__
```bash
nano /etc/systemd/system/my-service.service
```

Use the format
```
[Unit]
Description=My service server
After=network.target

[Service]
Type=simple
User=tars
ExecStart=/path/to/executable /path/to/config
WorkingDirectory=/path/to/working/dir
Restart=on-failure
RestartSec=10s
StandardOutput=file:/var/log/my-service/my-service.out
StandardError=file:/var/log/my-service/my-service.err
LimitNOFILE=800000
Environment=PATH=/usr/bin:/bin:/usr/local/bin

[Install]
WantedBy=multi-user.target
```



__Reload the daemon__
```bash
sudo systemctl daemon-reload
```

__Start the service__
```bash
sudo systemctl start zookeeper
```
In place of `start`:
- Use `stop` to stop the service
- Use `restart` to restart the service
- Use `status` to get the systemd status of the service


__Journal logs about the service__
```bash
journalctl -u zookeeper.service
```
