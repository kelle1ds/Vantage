from kafka import KafkaAdminClient, KafkaProducer
import json
from json import loads
from csv import DictReader

bootstrap_servers = ['localhost:9092']
topicname = 'sample-topic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

with open('dex-chart.csv') as new_obj:
    csv_dict_reader = DictReader(new_obj)
    for row in csv_dict_reader:
        ack = producer.send(topicname,json.dumps(row).encode('utf-8'))
        metadata = ack.get()
        print(metadata.topic, metadata.partition)
