#include <Servo.h>
#define HollaPin 53
Servo servo;
int state = 0;
int incomingByte;
const int ledPin = 13;
const int servoStopPWM = 88;

byte stage; //1..4 stages of height 

bool isHollaReached = false;

void setup()
{
  Serial.begin(9600);
  pinMode(HollaPin, INPUT);
  pinMode(ledPin, OUTPUT);
  servo.attach(3);
  servo.write(88);

  stage = 1;
}

void loop()
{  
  state = digitalRead(HollaPin);
  
  if(state == HIGH) digitalWrite(ledPin, LOW);
  if(state == LOW)  digitalWrite(ledPin, HIGH);


  
  
  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();
    if (incomingByte == 'B') StartServo();
    if(incomingByte == 'S') StopServo();
   }
}

void StopServo(){
  servo.write(servoStopPWM);
  Serial.write("Stoped\n");
}

void StartServo(bool up){
  if(up) servo.write(0);
  else servo.write(180);
  Serial.write("Started\n");
}
