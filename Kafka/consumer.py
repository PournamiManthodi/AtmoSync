from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "atmosync-climate",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for AtmoSync data...")

for message in consumer:

    record = message.value

    print(record)