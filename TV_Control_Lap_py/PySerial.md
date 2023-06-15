# PySerial

[Documentation](https://pyserial.readthedocs.io/en/latest/pyserial.html)

> Give you acess to any serial communication with the device
> 
> This summary only contain communication with arduino

## Installation

```cmd
pip install pyserial
```

---

## Importing

```python
import serial
```

--- 

### 1] Defining

```python
serial.Serial(port="com16", baudrate=9600)
```

- Open Serial Port

- > #### Arguments
  > 
  > - `port` Where arduino is connected
  > 
  > - `baudrate` refers to the number of bits per second that can be transferred between the Arduino and another device

> ##### Example
> 
> ```python
> import serial
> 
> port = "com16"
> baudRate = 9600
> 
> ard = serial.Serial(port="com16", baudrate=9600)
> ```
> 
> - If there is an error might be from:
> 
> - 1. Wrong port number
>   
>   2. Serial Monitor is open communicating with the arduino

---

### 2] Reading

```python
ard.readline().decode(encoding="utf-8").strip()
```

- To get the same output in python as in serial monitor

- `readline` return value in bytes

- `decode(encoding="utf-8")` convert bytes to utf-8 **[string]**

- `strip` built-in function that removes any leading or trailing whitespace from a string, whitespace characters include spaces, tabs and newlines

> ##### Example
> 
> - Arduino Code:
> 
> ```c
> #include <IRremote.hpp>
> 
> # define IR_RECEIVE_PIN 2
> 
> void setup()
> {
> 
>   IrReceiver.begin(IR_RECEIVE_PIN, DO_NOT_ENABLE_LED_FEEDBACK);
>   Serial.begin(9600);
> }
> 
> void loop() {
>   if (IrReceiver.decode()) {
>       Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
>       IrReceiver.resume(); 
>   }
> }
> ```
> 
> - Python Code:
> 
> ```python
> import serial
> 
> port = "com16"
> baudRate = 9600
> 
> ard = serial.Serial(port="com16", baudrate=9600)
> while True:
>     output = ard.readline().decode(encoding="utf-8").strip()
>     print(output)
> 
> ```
> 
> ```python
> F20DEF00
> 0
> EB14EF00
> 0
> EB14EF00
> 0
> ```

--- 

### 3] Sending


