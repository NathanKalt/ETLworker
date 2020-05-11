from kafka import KafkaProducer
import json
from time import sleep

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

i = 0
while True:
    i+=1
    producer.send('FEED', {'data': i})
    sleep(0.1)

