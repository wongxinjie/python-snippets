import msgpack
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'tungee-crm-bussiness',
    group_id='tungee-snail',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=msgpack.dumps
)

for message in consumer:
    print(message.topic, message.offset, message.key)
    value = message.value
    print(msgpack.loads(value))
