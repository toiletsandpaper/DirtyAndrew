/*
 Physical Pixel

An example of using the Arduino board to receive data from the
computer.  In this case, the Arduino boards turns on an LED when
it receives the character 'H', and turns off the LED when it
receives the character 'L'.

The data can be sent from the Arduino serial monitor, or another
program like Processing (see code below), Flash (via a serial-net
proxy), PD, or Max/MSP.

The circuit:
* LED connected from digital pin 13 to ground

created 2006
by David A. Mellis
modified 14 Apr 2009
by Tom Igoe and Scott Fitzgerald

This example code is in the public domain.

http://www.arduino.cc/en/Tutorial/PhysicalPixel
*/




//const int ledPin = 8; // the pin that the LED is attached to
int val;      // a variable to read incoming serial data into

void setup() {
 // initialize serial communication:
 Serial.begin(9600);
 // initialize the LED pin as an output:
 pinMode(8, OUTPUT);
 pinMode(13, OUTPUT);
}

void loop() {
 digitalWrite(13, HIGH);
 // see if there's incoming serial data:
 if (Serial.available()) {
   // read the oldest byte in the serial buffer:
   val = Serial.read();
   // if it's a capital H (ASCII 72), turn on the LED:
   if (val == 'H') {
     digitalWrite(8, HIGH);
   }
   // if it's an L (ASCII 76) turn off the LED:
   if (val == 'L') {
     digitalWrite(8, LOW);

//Serial.print('H');
// delay(1000);  
//Serial.print('L');  
//delay(1000);

   
   }
 }
}
