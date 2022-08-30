#!/usr/bin/env python3
import time
from gpiozero import CPUTemperature
from gpiozero import OutputDevice

ON_THRESHOLD = 55      # Temperature at which fan turns on (degrees C)
OFF_THRESHOLD = 45     # Temperature at which fan turns on (degrees C)
SLEEP_INTERVAL = 5     # Sleep interval between temperature checks (seconds)
GPIO_PIN = 17          # GPIO pin for fan control

def get_temp():
    """ Get CPU temperature
    return temperature value or runtime error
    """
    cpu = CPUTemperature()
    try:
        temp = cpu.temperature
        #print(temp)             
        return temp
    except:
        raise RuntimeError('Could not get temperature.')

fan = OutputDevice(GPIO_PIN)
print("fan.value =", str(fan.value))
fan.on()
print("Fan is on.")
print("fan.value =", str(fan.value))

time.sleep(SLEEP_INTERVAL)

