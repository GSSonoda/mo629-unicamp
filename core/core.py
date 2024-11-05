import os
from influxdb_client_3 import InfluxDBClient3

token = "4V0lbHBVWwmFGL8A1takTaNYsmhT_G_Pc3ZsYeCv5olkmEoRyYPrpS-CwwymJGp7Jhq7GR6geCWk8kF3uQBV1A=="
org = "Unicamp MO629"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"
database= "temp_data"

client = InfluxDBClient3(host=host, token=token, org=org)
