import serial

port = "com16"
baudRate = 9600

ard = serial.Serial(port="com16", baudrate=9600)
while True:
    output = ard.readline().decode(encoding="utf-8").strip()
    print(output)
