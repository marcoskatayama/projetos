#include <Arduino.h>

//Definindo os pinos
const int buttonPin = 2;
const int buttonPin2 = 3;
const int ledPin = 13;
const int speakerPin = 11;

int buttonState = 0;
int buttonState2 = 0;

void setup() {
  //Inicia o pino do LED como uma saída
  pinMode(ledPin, OUTPUT);
  //Inicia o pino do botão de pressão como uma entrada
  pinMode(buttonPin, INPUT);  
  pinMode(buttonPin2, INPUT);  
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  //Lê o estado do valor do botão de pressão
  buttonState = digitalRead(buttonPin);
  buttonState2 = digitalRead(buttonPin2);
  //Verifica se o botão de pressão está pressionado
  //Se estiver, buttonState é igual a HIGHT
  if(buttonState == HIGH){
    //Acende o LED
    digitalWrite(ledPin, HIGH);
    tone(speakerPin, 330);
  }else if (buttonState2 == HIGH) {
    digitalWrite(ledPin, HIGH);
    tone(speakerPin, 294);
  }else{
    //Desliga o alto-falante
    noTone(speakerPin);
    //Apaga o LED
    digitalWrite(ledPin, LOW);
    
  }
}