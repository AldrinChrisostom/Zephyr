void setup() {
  pinMode(3, OUTPUT);      // Timer02 output pin
    
  //Set frequency to 4MHz, 25% duty cycle
  TCCR2A = _BV(COM2A0) | _BV(COM2B1) | _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(WGM22) | _BV(CS20);
  OCR2A = 3;
  OCR2B = 0;

  Serial.begin(9600);
}

void loop() {

  int data = analogRead(0);
  int threshhold = 250;

  Serial.print(data);

//  if(data > threshhold){
//    Serial.print(true);
//    }
//    else{
//      Serial.print(false);
//    }
//  delay(1000);
// terst
  Serial.println();
}
