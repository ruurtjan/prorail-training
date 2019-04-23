from time import sleep
from json import dumps, load
from kafka import KafkaProducer
from glob import glob
import itertools

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))


def load_json(filename):
    with open(filename, 'r') as f:
        return load(f)


if __name__ == "__main__":
    # Load images
    image_names = glob('data/*.json')
    images = [load_json(x) for x in image_names]
    # Iterate over 10 images
    while True:
        for i in itertools.cycle(range(10)):
            producer.send('newImages', value=images[i])
            print("Sent {}".format(image_names[i]))
            sleep(2)
