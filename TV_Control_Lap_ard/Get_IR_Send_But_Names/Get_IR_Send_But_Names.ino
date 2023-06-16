#include <IRremote.hpp>

# define IR_RECEIVE_PIN 2

unsigned long data;

String butName;

void setup()
{

  IrReceiver.begin(IR_RECEIVE_PIN, DO_NOT_ENABLE_LED_FEEDBACK);
  Serial.begin(9600);
}

void loop() {
  if (IrReceiver.decode()) {
      data = IrReceiver.decodedIRData.decodedRawData;
      // Serial.println(data);
      IrReceiver.resume(); 

      switch(data){
        case 4211407875:
            butName = "Ok";
            break;
        case 3994156035:
            butName = "Power";
            break;
        case 4010867715:
            butName = "Mute";
            break;
        case 3075013635:
            butName = "VolumeUp";
            break;
        case 2991455235:
            butName = "VolumeDown";
            break;
        case 3091725315:
            butName = "Up";
            break;
        case 3024878595:
            butName = "Down";
            break;
        case 2891185155:
            butName = "Right";
            break;
        case 2824338435:
            butName = "Left";
            break;
        case 3158572035:
            butName = "Menu";
            break;
        case 2907896835:
            butName = "Exit";
            break;
        case 3960732675:
            butName = "Info";
            break;
        case 2807626755:
            butName = "F1";
            break;
        case 2874473475:
            butName = "F2";
            break;
        case 2740780035:
            butName = "F3";
            break;
        case 2958031875:
            butName = "F4";
            break;
        case 2690644995:
            butName = "Play-Pause";
            break;
        case 3141860355:
            butName = "Forward";
            break;
        case 3910597635:
            butName = "Backward";
            break;
        case 4144561155:
            butName = "ScrollUp";
            break;
        case 2707356675:
            butName = "ScrollDown";
            break;
        
        // default:
        //     butName = "Nothing";
        //     break;
      }

      Serial.println(butName);
  }
}