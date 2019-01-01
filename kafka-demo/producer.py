import msgpack
from kafka import KafkaProducer

messages = [
    {"action": "update", "bussiness_type": "lead",
     "bussiness_doc_id": "aaaaa", "context": {"name": "aaaa"}}
]

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=msgpack.dumps,
)

for msg in messages:
    producer.send('tungee-crm-business', msg)
