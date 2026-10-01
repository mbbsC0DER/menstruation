# python3 -m venv <name>
# source <name>/bin/activate
# pip install RPi.GPIO

# Practical 7: IoT Based Web Controlled Home Automation
# Raspberry Pi Relay Control
#
# Relay connection:
# Relay IN  -> Raspberry Pi Physical Pin 37
# Relay GND -> Raspberry Pi GND pin 6
# Relay VCC -> Appropriate supply for relay module pin 2
#
#
# Run:
# python home_pract7.py

import RPi.GPIO as GPIO
from time import sleep

relay_pin = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)

GPIO.output(relay_pin, 1)

try:
    while True:
        GPIO.output(relay_pin, 0)
        sleep(5)

        GPIO.output(relay_pin, 1)
        sleep(5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
