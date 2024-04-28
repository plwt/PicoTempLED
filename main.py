import machine
import utime
from machine import Timer

## Temperature sensor
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)

## Convert to Celsius
conversion_factor = 3.3 / (65535)


## Setup the onboard LED
led_onboard = machine.Pin(25, machine.Pin.OUT)

## Setup the onboard LED for off
def leds_off():
    """Turn off all the LEDs."""
    led_onboard.value(0)

## Setup the onboard LED for on
def leds_on():
    """Turn on all the LEDs."""
    led_onboard.value(1)

## Read the temperature, write to file, and turn on the LED
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    
    ## Minimum temperature
    if temperature <= 12.00:
        leds_off()
        led_onboard.value(1)
    
    ## Maximum temperature
    elif temperature > 28.00:
        leds_off()
        led_onboard.value(1)
    
    ## Outside of the range, turn off the LED
    else:
        leds_off()







python
import machine
import time
import dht

# Configure the temperature sensor
sensor = dht.DHT11(machine.Pin(4))  # Assuming the sensor is connected to GPIO 4

# Configure the LED
led = machine.Pin(2, machine.Pin.OUT)  # Assuming the LED is connected to GPIO 2

# Set the temperature threshold (in Celsius)
temperature_threshold = 30

while True:
    try:
        sensor.measure()  # Trigger a temperature measurement
        temperature = sensor.temperature()  # Get the temperature in Celsius

        if temperature > temperature_threshold:
            # Blink the LED if temperature exceeds the threshold
            led.value(1)  # Turn on the LED
            time.sleep(0.5)  # Wait for 0.5 seconds
            led.value(0)  # Turn off the LED
            time.sleep(0.5)  # Wait for 0.5 seconds
        else:
            led.value(0)  # Keep the LED off

        print("Temperature: {:.1f} °C".format(temperature))

    except OSError as e:
        print("Error: {}".format(e))

    time.sleep(2)  # Wait for 2 seconds before taking the next measurement



