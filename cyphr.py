#!/usr/bin/env python3
import serial
import time
sensor1=[]


communi = serial.Serial("/dev/ttyUSB0", 9600, timeout = 1.0)

time.sleep(3)

communi.reset_input_buffer()
print("Serial OK")
try:
    while True:
        time.sleep(0.01)
        if communi.in_waiting>0:
            line = communi.readline().decode("utf-8")
            li= communi.readline().decode("utf-8")
            print(line)
            if line not in sensor1:
                sensor1.append(line)
                print("sensor1:",sensor1)

                
except KeyboardInterrupt:
    print("closing serial communication")
    communi.close()
