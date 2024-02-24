# MasterClass-Dashboards
Scripts and some background information for the Masterclass Dashboards held during the Data-Driven Duurzaam in Manufacturing meeting [20240228]

## circuitpython
Code running on the [picopi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html). All the files in this folder are already present on the device. At the school nothing has to be done.

If you want to run the device on another network, change the `settings.toml` file (a normal text file, editable by [notepad++](https://notepad-plus-plus.org/) or any other text-editor), specifically:
 * `WIFI_SSID`
 * `WIFI_PASSWORD`
The other settings can be changed if you move to another MQTT-broker.

If you want to do something completely different with the device, [Pico Projects](https://projects.raspberrypi.org/en/projects/get-started-pico-w) is a nice place to start.

### Dependencies
The code relies on the Adafruit Circuitpython MQTT library:
 * [Adafruit miniMQTT](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT)

## Dashboard
Running the dashboard in the cloud, with only a dependency on [HiveMQ](https://hivemq.com) makes it impossible to store data or look back at certain time intervals. There is no data storage, only a stream of data from the sensor to the Grafana dashboard. 

If you want to store the data a database setup is required. One option is [influxdb](https://influxdata.com). They provide a cloud-version (paid), but also a open-source version which can be configured using [Docker](https://docker.io) containers. There are many guides on the internet on configuring a MQTT broker, database and visualization program on a (home)server. For example [MQTT - Influx - Grafana](https://wirelessthings.io/index.php/2023/01/31/telegraf-influxdb-grafana-with-docker-compose/).
 
For this demonstration project the configuration of docker and setting up the servers is too advanced. 
