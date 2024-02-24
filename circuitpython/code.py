# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import sys
import ssl
import ipaddress
import wifi
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import microcontroller
import time

print("Connecting to WiFi")

#  connect to your SSID
try:
    wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))
except:
    print("could not connect to SSID")
    sys.exit()

mac = ''.join(['{:>02s}'.format(hex(ii)[2:]) for ii in wifi.radio.mac_address])
print('mac address: ', mac)

pool = socketpool.SocketPool(wifi.radio)

mqtt_topic = os.getenv('MQTT_topic') + '/' + mac
mqtt_client = MQTT.MQTT(
    broker=os.getenv('HIVE_cluster_url'),
    username=os.getenv('HIVE_username'),
    password=os.getenv('HIVE_password'),
    port = os.getenv('HIVE_port'),
    socket_pool=pool,
    is_ssl=True,
    ssl_context = ssl.create_default_context()
)

errors = 0
run = True
while run:
    try:
        mqtt_client.connect()
        mqtt_client.publish(mqtt_topic, microcontroller.cpu.temperature)
        errors = 0 # reset counters, no erros in communcating with mqtt
    except KeyboardInterrupt:
        run =  False
    except:
        print('error in MQTT connect and/or publish')
        print('will try again (for the %d time)...' %(errors))
        errors += 1
        if errors > 10:
            sys.exit()
        pass
    time.sleep(5)
