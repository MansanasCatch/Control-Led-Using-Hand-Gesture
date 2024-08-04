import serial as s
import time as t
ser = s.Serial('COM3', 9600, timeout=0)   # check your com port
t.sleep(2)
print(ser.name,"connected")

def led(finger):
    print(finger)
    ser.write(finger.encode())
