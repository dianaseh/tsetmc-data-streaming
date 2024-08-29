import json
from kafka import KafkaConsumer
from datetime import datetime
import os

# kafka topic name
topic_name = "tsetmc"
# initializing the kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Create the 'raw' directory if it doesn't exist
if not os.path.exists('raw'):
    os.makedirs('raw')
# consume the messages and write to JSON files
for message in consumer:
    data = message.value
    filename = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".json"
    with open(f"raw/{filename}", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)