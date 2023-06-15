#include <IRremote.hpp>

# define IR_RECEIVE_PIN 2

void setup()
{

  IrReceiver.begin(IR_RECEIVE_PIN, DO_NOT_ENABLE_LED_FEEDBACK);
  Serial.begin(9600);
}

void loop() {
  if (IrReceiver.decode()) {
      Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
      IrReceiver.resume(); 
  }
}