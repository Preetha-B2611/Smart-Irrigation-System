```python
from machine import Pin, ADC
from time import sleep

# Soil moisture sensor connected to GP26 (ADC0)
moisture_sensor = ADC(Pin(26))

# Relay module connected to GP15
relay = Pin(15, Pin.OUT)

# Set relay OFF initially (active-low relay)
relay.value(1)

# Moisture thresholds (calibrate for your sensor)
DRY_THRESHOLD = 42000
WET_THRESHOLD = 30000

pump_on = False

while True:
    # Read soil moisture sensor
    moisture = moisture_sensor.read_u16()

    print("Soil Sensor Value:", moisture)

    # Turn ON pump when soil is dry
    if moisture > DRY_THRESHOLD and not pump_on:
        relay.value(0)
        pump_on = True
        print("Soil is dry - Water pump ON")

    # Turn OFF pump when soil has enough moisture
    elif moisture < WET_THRESHOLD and pump_on:
        relay.value(1)
        pump_on = False
        print("Soil is moist - Water pump OFF")

    else:
        print("Pump Status:", "ON" if pump_on else "OFF")

    sleep(2)
```
