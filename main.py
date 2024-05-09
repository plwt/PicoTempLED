import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)
reading = sensor_temp.read_u16() * conversion_factor
temperature = 27 - (reading - 0.706)/0.001721


while True:
    if temperature > 30:
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(3)

