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