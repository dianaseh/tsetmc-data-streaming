import requests_html
from kafka import KafkaProducer
from json import dumps
from time import sleep

# clean the data, so it only includes the fields shown in the market map page (in similar order)
def clean_data(raw_data):
    cleaned_data = []
    for entry in raw_data:
        cleaned_entry = {
            'lSecVal': entry['lSecVal'],
            'lVal30': entry['lVal30'],
            'lVal18AFC': entry['lVal18AFC'],
            'pClosing': entry['pClosing'],
            'percent': entry['percent'],
            'pDrCotVal': entry['pDrCotVal'],
            'priceChangePercent': entry['priceChangePercent'],
            'zTotTran': entry['zTotTran'],
            'qTotTran5J': entry['qTotTran5J'],
            'qTotCap': entry['qTotCap'],
            'hEvenShow': entry['hEvenShow']
        }
        cleaned_data.append(cleaned_entry)
    return cleaned_data

# Kafka topic name
topic_name = "tsetmc"
# Initializing the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8'))
# Establish a session and retrieve data using api
session = requests_html.HTMLSession()
api_url = 'http://cdn.tsetmc.com/api/ClosingPrice/GetMarketMap?market=0&size=1360&sector=0&typeSelected=1'

# Get and send the data through the kafka topic every 5 seconds
while True:
    json = session.get(api_url).json()
    producer.send(topic_name, clean_data(json))
    sleep(5)
