#!/usr/bin/env python3
# Use gpiozero to read CPU temperature and control fan.
# Use threshold values for on and off and use a gpio output
# pin to turn a transistor on and off to control the fan.
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

if __name__ == '__main__':
    # Validate the on and off thresholds
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    fan = OutputDevice(GPIO_PIN)

    while True:
        temp = get_temp()
        
        # Turn the fan on if the temperature has reached the threshold
        # and the fan is off.
        # NOTE: fan.value returns 1 for "on" and 0 for "off"
        if temp > ON_THRESHOLD and not fan.value:
            fan.on()
            #print("Fan ON")
            
        # Turn the fan off if the fan is ong and the temperature has
        # dropped below lower threshold. 
        elif fan.value and temp < OFF_THRESHOLD:
            fan.off()
            #print("Fan OFF")
            
        time.sleep(SLEEP_INTERVAL)

