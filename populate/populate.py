import time
import random

from influxdb_client_3 import Point
from core.core import client, database

data_example = {
    "point1": {
        "node": "node1",
        "latitude": "-22.813511570212142",
        "longitude": "-47.06393397533617",
        "temperature": random.choice([22, 23, 24]),
    },
    "point2": {
        "node": "node1",
        "latitude": "-22.813511570212142",
        "longitude": "-47.06393397533617",
        "temperature": random.choice([22, 23, 24]),
    },
    "point3": {
        "node": "node1",
        "latitude": "-22.813511570212142",
        "longitude": "-47.06393397533617",
        "temperature": random.choice([22, 23, 24]),
    },
    "point4": {
        "node": "node1",
        "latitude": "-22.813511570212142",
        "longitude": "-47.06393397533617",
        "temperature": random.choice([22, 23, 24]),
    },
    "point5": {
        "node": "node1",
        "latitude": "-22.813511570212142",
        "longitude": "-47.06393397533617",
        "temperature": random.choice([22, 23, 24]),
    },
    "point6": {
        "node": "node1",
        "latitude": "-22.813511570212142",
        "longitude": "-47.06393397533617",
        "temperature": random.choice([22, 23, 24]),
    },
}

def populate():

  for key in data_example:
    point = (
      Point("temperature")
      .tag("node", data_example[key]["node"])
      .field("latitude", data_example[key]["latitude"])
      .field("longitude", data_example[key]["longitude"])
      .field("temperature", data_example[key]["temperature"])
    )
    client.write(database=database, record=point)
    time.sleep(1) # separate points by 1 second

  print("Complete. Return to the InfluxDB UI.")
