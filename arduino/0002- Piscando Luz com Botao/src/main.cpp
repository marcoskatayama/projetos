#include <Arduino.h>

//Definindo os pinos
const int buttonPin = 2;
const int ledPin = 13;

int buttonState = 0;

void setup() {
  //Inicia o pino do LED como uma saída
  pinMode(ledPin, OUTPUT);
  //Inicia o pino do botão de pressão como uma entrada
  pinMode(buttonPin, INPUT);  
}

void loop() {
  //Lê o estado do valor do botão de pressão
  buttonState = digitalRead(buttonPin);

  //Verifica se o botão de pressão está pressionado
  //Se estiver, buttonState é igual a HIGHT
  if(buttonState == HIGH){
    //Acende o LED
    digitalWrite(ledPin, HIGH);
  }else{
    //Apaga o LED
    digitalWrite(ledPin, LOW);
  }
}