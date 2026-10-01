# python3 -m venv <name>
# source <name>/bin/activate
# pip install pyserial pynmea2 RPi.GPIO

# Practical 5: Raspberry Pi GPS Module Interfacing
#
# Serial Port: /dev/ttyAMA0
# Baud Rate: 9600
#
# Setup:
# sudo nano /boot/config.txt
#
# VCC  ─────────→  Power pin 2
# GND  ─────────→  Pin 6
# TX   ─────────→  Pin 10
#
# Add:
# dtparam=spi=on
# dtoverlay=pi3-disable-bt
# core_freq=250
# enable_uart=1
# force_turbo=1
#
# Then:
# sudo systemctl stop serial-getty@ttyS0.service
# sudo systemctl disable serial-getty@ttyS0.service
# sudo systemctl enable serial-getty@ttyAMA0.service
#
# Install:
# sudo apt-get install minicom
#
# Run:
# python gps_pract4.py

# Run either the short or long example separately; the short loop runs continuously.
# Short Form Code
import serial
import pynmea2

port = "/dev/ttyAMA0"

ser = serial.Serial(
    port,
    baudrate=9600,
    timeout=0.5
)

while True:
    data = ser.readline()

    if data[0:6] == b'$GPGGA':
        msg = pynmea2.parse(data.decode())
        print(msg)


# Long Form Code
import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

port = "/dev/ttyAMA0"

# Create serial object
ser = serial.Serial(
    port,
    baudrate=9600,
    timeout=0.5
)

while True:
    try:
        data = ser.readline()
    except:
        print("loading")

    if data[0:6] == b'$GPGGA':
        msg = pynmea2.parse(data.decode(errors="ignore"))
        print(msg)
        time.sleep(2)
