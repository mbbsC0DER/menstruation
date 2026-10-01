# python3 -m venv <name>
# source <name>/bin/activate
# pip install RPi.GPIO

# Practical 1: Displaying LED Pattern using Raspberry Pi
#
# Connection:
# LED long leg (+)  -> Physical Pin 11
# LED short leg (-) -> Physical Pin 6 (GND)
#
#
# Run:
# python led_pract1.py

import RPi.GPIO as GPIO
import time

numTimes = int(input("Enter total number of times to blink: "))
speed = float(input("Enter length of each blink (seconds): "))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

def Blink(numTimes, speed):
    for i in range(numTimes):
        print("Iteration", i + 1)

        GPIO.output(11, True)
        time.sleep(speed)

        GPIO.output(11, False)
        time.sleep(speed)

Blink(numTimes, speed)

GPIO.cleanup()
print("Done")
