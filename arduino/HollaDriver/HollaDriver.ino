#define HollaPin 22
int state = 0;

const int ledPin = 13;

void setup()
{
  Serial.begin (9600);
  pinMode(HollaPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop()
{  
  state = digitalRead(HollaPin);

  Serial.write(state);
  
  if(state == HIGH) digitalWrite(ledPin, LOW);
  if(state == LOW)  digitalWrite(ledPin, HIGH);
}
