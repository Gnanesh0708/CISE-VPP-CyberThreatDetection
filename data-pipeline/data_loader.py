import io
import pandas as pd
import requests
#import paho.mqtt.client as mqtt
#import matplotlib.pyplot as plt
import datetime
import json
import socket
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

'''# MQTT settings
broker_address = "iot.reyax.com"
port = 1883
username = "RRvErKBFat"
password = "P9Ce4gWkVy"

def get_ip_address_ports():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((broker_address, port))
    source_ip, source_port = s.getsockname()
    destination_ip, destination_port = s.getpeername()
    s.close()
    return source_ip, source_port, destination_ip, destination_port

source_ip, source_port, destination_ip, destination_port = get_ip_address_ports()

# Data storage lists
data_storage = {
    "pv_voltage": [],
    "pv_current": [],
    "battery_voltage": [],
    "battery_current": [],
    "soc": [],
    "pcc_voltage": [],
    "pcc_current": [],
    "three_p_voltage": [],
    "three_p_current": [],
    "cyber_threat": [],
    "timestamp": [],
    "length": [],
    "ip_address_ports": []
}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    topics = [
        "pv_voltage", "pv_current", "battery_voltage", "battery_current", 
        "SOC", "pcc_voltage", "pcc_current", "three_p_voltage", 
        "three_p_current", "cyber_threat"
    ]
    for topic in topics:
        client.subscribe(topic)

# Lists to store the data for each topic
data = {
    'timestamp': [],
    'pv_voltage': [],
    'pv_current': [],
    'battery_voltage': [],
    'battery_current': [],
    'SOC': [],
    'pcc_voltage': [],
    'pcc_current': [],
    'three_phase_voltage': [],
    'three_phase_current': [],
    'cyber_threat': [],
    'length': [],
    'ip_adress_and_ports': [],
    'protocol':[]
}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    topics = [
        "pv_voltage", "pv_current", "battery_voltage", "battery_current",
        "SOC", "pcc_voltage", "pcc_current", "three_p_voltage",
        "three_p_current", "cyber_threat"
    ]
    for topic in topics:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    value = float(msg.payload.decode())
    current_time = datetime.datetime.now()
    msg_length = len(msg.payload.decode())

    data['timestamp'].append(current_time)
    data['length'].append(msg_length)
    data['ip_adress_and_ports'].append((source_ip, source_port, destination_ip, destination_port))
    data['protocol'].append('MQTT')

    if msg.topic == "pv_voltage":
        data['pv_voltage'].append(value)
    elif msg.topic == "pv_current":
        data['pv_current'].append(value)
    elif msg.topic == "battery_voltage":
        data['battery_voltage'].append(value)
    elif msg.topic == "battery_current":
        data['battery_current'].append(value)
    elif msg.topic == "SOC":
        data['SOC'].append(value)
    elif msg.topic == "pcc_voltage":
        data['pcc_voltage'].append(value)
    elif msg.topic == "pcc_current":
        data['pcc_current'].append(value)
    elif msg.topic == "three_p_voltage":
        data['three_phase_voltage'].append(value)
    elif msg.topic == "three_p_current":
        data['three_phase_current'].append(value)
    elif msg.topic == "cyber_threat":
        data['cyber_threat'].append(value)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port, 60)

# Run the loop for 5 minutes
start_time = time.time()
try:
    while time.time() - start_time < 5 * 60:
        client.loop()
except KeyboardInterrupt:
    pass
finally:
    timestamp = data['timestamp'][:len(data["pv_voltage_data"])]
    length = data["length"][:len(data["pv_voltage_data"])]
    ip_address_ports = data["ip_address_ports"][:len(data["pv_voltage_data"])]
    pv_current_data = data["pv_current_data"][:len(data["pv_voltage_data"])]
    battery_voltage_data = data["battery_voltage_data"][:len(data["pv_voltage_data"])]
    df = pd.DataFrame(data_dict)
'''
@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = '/home/src/mqtt_data/dynamic_model_mqtt.csv'

    return pd.read_csv(url, sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
