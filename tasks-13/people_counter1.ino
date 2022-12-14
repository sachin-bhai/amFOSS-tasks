#include <LiquidCrystal.h>

//initialize the pins
const int trigPin = 6;
const int echoPin = 7;
const int buzzer = 8;
int count = 0;

//initialize the variables
long duration;
int distance;

//interfacing the LCD display
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup()
{
 //setup code to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzer, OUTPUT);
  
  lcd.begin(16,2);
  lcd.clear();
  Serial.begin(9600);
}

void loop()
{
  lcd.clear();
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin,LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2)/29.1;
  delay(500);
  
  //suppose I have fixed the ultrasonic senser at the distance of 100 cm
  if (distance <100)
  {
    tone(buzzer,200);
    count++;
  }
  else 
  {
    noTone(buzzer);
  }
  
  lcd.clear();
  lcd.print("Distance: ");
  lcd.print(distance);
  lcd.print("cm");
  lcd.setCursor(0,1);
  lcd.print("No. of Person:");
  lcd.print(count);
  delay(1000);
  Serial.print("Distance");
  Serial.print(distance);
  Serial.print("cm");
  delay(1000);
}