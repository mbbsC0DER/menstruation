# python3 -m venv <name>
# source <name>/bin/activate
# pip install tm1637 RPi.GPIO

# Practical 2: Display Time over 4-Digit 7-Segment Display
#
# Connection:
# TM1637 CLK -> Physical Pin 16
# TM1637 DIO -> Physical Pin 18
# TM1637 VCC -> 5V pin 2
# TM1637 GND -> GND pin 6
#
#

# PIN NUMBERING NOTE:
# The common raspberrypi-tm1637 driver uses GPIO.BCM internally:
#   clk=23, dio=24 -> PHYSICAL pins 16 and 18, matching the wiring above.
# Driver source: https://github.com/depklyon/raspberrypi-tm1637/blob/master/tm1637.py
# See raspberry_pi_4b_pinout.md for the complete header mapping.
#

import time
import datetime
import tm1637

Display = tm1637.TM1637(clk=23, dio=24)

Display.write([0, 0, 0, 0])
Display.brightness(1)

while True:
    now = datetime.datetime.now()

    hour = now.hour
    minute = now.minute
    second = now.second

    show_colon = (second % 2 == 0)

    Display.numbers(hour, minute, colon=show_colon)

    time.sleep(1)
