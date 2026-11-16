import gc
import machine
import utime

# Temperature sensor and onboard LED (Raspberry Pi Pico / RP2040).
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
led = machine.Pin(25, machine.Pin.OUT)

# Convert a 16-bit ADC reading to volts.
conversion_factor = 3.3 / 65535

MIN_TEMP_C = 12.0
MAX_TEMP_C = 28.0
SAMPLE_COUNT = 3
SAMPLE_DELAY_MS = 10
BLINK_MS = 500
LOOP_DELAY_MS = 5000
GC_INTERVAL = 60


def read_temperature_c():
    """Return the averaged onboard temperature sensor reading in Celsius."""
    reading_total = 0
    for _ in range(SAMPLE_COUNT):
        reading_total += sensor_temp.read_u16()
        utime.sleep_ms(SAMPLE_DELAY_MS)

    reading = (reading_total / SAMPLE_COUNT) * conversion_factor
    return 27 - (reading - 0.706) / 0.001721


def blink_led():
    """Blink once to indicate a temperature outside the configured range."""
    led.value(1)
    utime.sleep_ms(BLINK_MS)
    led.value(0)


# Start in a known state and reclaim any available heap before the main loop.
led.value(0)
gc.enable()
gc.collect()
loop_count = 0

while True:
    try:
        temperature = read_temperature_c()

        if temperature <= MIN_TEMP_C or temperature > MAX_TEMP_C:
            blink_led()
        else:
            led.value(0)
    except Exception:
        # Fail safely: a failed reading should not leave the LED on.
        led.value(0)
        gc.collect()
        utime.sleep_ms(LOOP_DELAY_MS)
        continue

    loop_count += 1
    if loop_count >= GC_INTERVAL:
        gc.collect()
        loop_count = 0

    utime.sleep_ms(LOOP_DELAY_MS)
