import serial

port = "com16"
baudRate = 9600

ard = serial.Serial(port="com16", baudrate=9600)
while True:
   code_ = ard.readline().decode(encoding="utf-8").strip()
   print(code_)
   print(type(ard.readline()))
   print(type(ard.readline().decode(encoding="utf-8")))
