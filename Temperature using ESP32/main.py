from machine import Pin,SoftI2C
import dht
import time
import ssd1306

i2c = SoftI2C(scl=Pin(22),sda=Pin(21))

oled = ssd1306.SSD1306_I2C(128,64,i2c)

sensor_data=dht.DHT22(Pin(15))

def call_dht():
    sensor_data.measure()
    global temp
    global hum
    temp=sensor_data.temperature()
    hum=sensor_data.humidity()
    print("Temperature - ",temp,"Humidity - ",hum)

while True:
    call_dht()
    oled.text("Temp-",0,0)
    oled.text(str(temp),50,0)
    oled.text("Hum-",0,10)
    oled.text(str(hum),50,10)
    oled.text("Made By-",0,20)
    oled.text("Kamallochan",20,30)
    oled.show()
    time.sleep(1)
    