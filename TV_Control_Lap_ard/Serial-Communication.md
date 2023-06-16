# Serial-Communication

[Serial - Arduino Reference](https://www.arduino.cc/reference/en/language/functions/communication/serial/)

> Used for communication between the Arduino board and a computer or other devices

## 1] Serial.begin

```c
Serial.begin(9600);
```

- Sets the data rate in bits per second (baud) for serial data transmission

## 2] Serial.available

```c
if (Serial.available() > 0) {....}
```

- Checks if there is data available on the serial port. If there is, the code inside `{...}` will run

## 3] Serial.println

```c
Serial.println("Hello World");
```

## 4] Serial.readString

```c
String input = Serial.readString();
```

- Return string of what is typed in the Serial Monitot

```c
input.trim();
```

- Remove any \r \n whitespace at the end of the String

> ##### Example
> 
> ```c
> # define led 13
> 
> void setup() {
>   // put your setup code here, to run once:
>   pinMode(led, OUTPUT);
>   Serial.begin(9600);
> 
> }
> 
> void loop() {
>   // put your main code here, to run repeatedly:
>   if (Serial.available() > 0){
>     String input = Serial.readString();
>     input.trim();
>     if (input=="on"){
>       Serial.println("The led is on");
>       digitalWrite(led, HIGH);
>       }
>     else if (input=="off"){
>       Serial.println("The led is off");
>       digitalWrite(led, LOW);
>     }
>     else{
>       Serial.println("No such command");
>     }
> }
> }
> 
> ```
> 
> ```c
> The led is on
> The led is off
> No such command
> The led is on
> No such command
> The led is off
> ```

--- 


