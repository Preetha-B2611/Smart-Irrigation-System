# Smart Irrigation System 🌱

## Project Overview
The Smart Irrigation System is an automated watering solution developed using Raspberry Pi Pico, MicroPython, and a soil moisture sensor. It monitors soil moisture levels and automatically controls a water pump to supply water when the soil becomes dry.

## Objectives
- Automate the irrigation process.
- Monitor soil moisture in real time.
- Reduce unnecessary water consumption.
- Minimize manual intervention.

## Hardware Requirements
- Raspberry Pi Pico
- Analog soil moisture sensor
- Relay module
- DC water pump
- External power supply
- Jumper wires

## Software Requirements
- Thonny IDE
- MicroPython firmware
- Raspberry Pi Pico

## Working Principle
1. The soil moisture sensor measures the moisture level.
2. The Raspberry Pi Pico reads the analog sensor output.
3. When the soil becomes dry, the Pico activates the relay.
4. The relay switches on the water pump.
5. When the soil reaches the required moisture level, the pump switches off automatically.

## Pin Connections

| Component | Pico Pin |
|---|---|
| Soil sensor analog output | GP26 / ADC0 |
| Relay input | GP15 |
| Sensor ground | GND |
| Sensor power | 3.3V, if supported |

Connect the pump through a suitably rated relay or driver and a separate power supply. Never power the pump directly from a Pico GPIO pin.

## How to Run
1. Install Thonny IDE.
2. Connect the Raspberry Pi Pico to your computer.
3. Select the Raspberry Pi Pico MicroPython interpreter.
4. Upload `main.py` to the Pico.
5. Run the program and monitor sensor readings in the Shell.
6. Calibrate the moisture thresholds for your sensor and soil.

## Future Improvements
- Add a water-level sensor.
- Add a maximum pump runtime for safety.
- Display moisture readings on an LCD or web dashboard.
- Add IoT-based remote monitoring.

## Applications
- Home gardens
- Small-scale agriculture
- Greenhouses
- Water-efficient irrigation systems

## Author
Preetha B

## Technologies Used
Python | MicroPython | Raspberry Pi Pico | Sensors | Embedded Systems
