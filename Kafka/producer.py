from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

df = pd.read_csv(
    "../data/AtmoSync_Micro_Climate_Analytics_12000.csv"
)

topic = "atmosync-climate"

for _, row in df.iterrows():

    record = row.to_dict()

    producer.send(topic, value=record)

    print("Sent:", record["Record_ID"])

    time.sleep(1)

producer.flush()
