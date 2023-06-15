# IRremote

[Documentation](https://github.com/Arduino-IRremote/Arduino-IRremote#readme)

> Send and receive infrared signals

---

# 1] Start

```c
#include <IRremote.hpp>
```

- To include the library into the code after installing a version of your choice

```c
# define IR_RECEIVE_PIN 2
```

- Arduino pin number connected to the output pin of IRreceviver

---

# 2] Setup

```c
IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
```

- Start the receiver

> #### Arguments
> 
> `IR_RECEIVE_PIN` IR pin number, Declared above
> 
> `ENABLE_LED_FEEDBACK` To turn on 13 pin led when receiving a signal
> 
> `DO_NOT_ENABLE_LED_FEEDBACK` Use it to turn off 13 pin led

```c
Serial.begin(9600);
```

- To make serial communication between arduino and pc, to send and receive data via cable

- Outputs and Inputs through Serial Monitor

---

## 3] Loop

```c
IrReceiver.decode()
```

- Return `0` or `1` 

- `0` No signal received

- `1` Signal received

```c
IrReceiver.resume();
```

- Enable receiving of the next value

> #### Example
> 
> ```c
> #include <IRremote.hpp>
> 
> # define IR_RECEIVE_PIN 2
> 
> void setup() {
>   IrReceiver.begin(IR_RECEIVE_PIN, DO_NOT_ENABLE_LED_FEEDBACK);
>   Serial.begin(9600);
> }
> 
> void loop() {
>   bool x = IrReceiver.decode();
>   Serial.println(x);
>   if (x){
>     Serial.println("I have received a signal");
>     IrReceiver.resume();
>   }
>   else{
>     Serial.println("No signal");
>   }
> }
> ```
> 
> ```c
> 0
> No signal
> 1
> I have received a signal
> 0
> No signal
> 0
> No signal
> ...
> ..
> .
> ```

```c
IrReceiver.decodedIRData.decodedRawData
```

- Return raw data of received signal

> #### Example
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
> ```c
> 0
> F30CEF00
> F708EF00
> 0
> FB04EF00
> 0
> ```
> 
> - Data is converted to HEX code
> 
> - Hex code is easier for humans to read than binary

---

## Extra

```c
#include <IRremote.hpp>

# define IR_RECEIVE_PIN 2

void setup(){

  IrReceiver.begin(IR_RECEIVE_PIN, DO_NOT_ENABLE_LED_FEEDBACK); // Start the receiver
  Serial.begin(9600);
}

void loop() {

  if (IrReceiver.decode()) {
      Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX); // Print "old" raw data
      // USE NEW 3.x FUNCTIONS
      IrReceiver.printIRResultShort(&Serial); // Print complete received data in one line
      IrReceiver.printIRSendUsage(&Serial);   // Print the statement required to send this data

      IrReceiver.resume(); // Enable receiving of the next value
  }  
}
```

- Code is slightly modified from the following [Code](https://github.com/Arduino-IRremote/Arduino-IRremote/tree/master#new-4x-program) in the official [Documentation](https://github.com/Arduino-IRremote/Arduino-IRremote#readme)

---
