import time
from machine import Pin

print("Hello, ESP32!")

led = Pin(2, Pin.OUT)
counter = 0
while True:
  led.value(1)
  time.sleep(0.5)
  led.value(0)
  time.sleep(0.5)
  counter += 1
  print("Blink", counter)
