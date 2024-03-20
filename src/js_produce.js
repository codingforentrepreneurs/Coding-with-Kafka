const { Kafka } = require("kafkajs")

const KAFKA_BROKER_URL="127.0.0.1:19092"
const KAFKA_TOPIC="hello-world"

const kafka  = new Kafka({
    clientId: 'my-node-app',
    brokers: [KAFKA_BROKER_URL]
})


async function main() {
    const producer = kafka.producer()
    // await 
    await producer.connect()
    const data = {hello: "js_world"}
    const dataJson = JSON.stringify(data)
    await producer.send({
        topic: KAFKA_TOPIC,
        messages: [
            {value: dataJson}
        ]
    })
    await producer.disconnect()

}


main().then(x=>console.log(x)).catch(err=>console.log(err))