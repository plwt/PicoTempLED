import machine
import utime

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
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(3)
    
    ## Maximum temperature
    elif temperature > 28.00:
        leds_off()
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(3)
    
    ## Outside of the range, turn off the LED
    else:
        leds_off()

    ## Sleep for 5 seconds.
    utime.sleep(5)