const { Kafka } = require("kafkajs")

const KAFKA_BROKER_URL="127.0.0.1:19092"
const KAFKA_TOPIC="hello-world"

const kafka  = new Kafka({
    clientId: 'my-node-app',
    brokers: [KAFKA_BROKER_URL]
})

async function handleMessage({topic, partition, message}) {
    const messageValue = message.value.toString()
    console.log(messageValue)
}

async function main() {
    const consumer = kafka.consumer({groupId: "nodejs"})
    // await 
    await consumer.connect()
    await consumer.subscribe({topic: KAFKA_TOPIC, fromBeginning: true})
    await consumer.run({
        eachMessage: handleMessage
    })

}


main().then(x=>console.log(x)).catch(err=>console.log(err))