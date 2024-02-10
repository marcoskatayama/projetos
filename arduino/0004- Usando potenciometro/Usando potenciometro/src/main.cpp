#include <Arduino.h>

const int analogInPin = A0; // Pino de entrada analógica ligado ao potenciometro
const int analogOutPin = 9; // Piono de saída analógica ligado ao led

int sensorValue = 0;        // Valor lido do potenciometro
int outputValue = 0;        // Valor enviado para o PWM(saída analógica)

void setup() {
  // Inicia a comunicação serial a 9600 bps:
  Serial.begin(9600);
}

void loop() {
  // Lê o valor analógico
  sensorValue = analogRead(analogInPin);
  // Mapeia esse valor no intervalo de saída analógica
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  // Muda o valor da saída analógica
  analogWrite(analogOutPin, outputValue);

  // Envia os resultados para o monitor serial
  Serial.print("sensor= ");
  Serial.print(sensorValue);
  Serial.print("\t output= ");
  Serial.println(outputValue);

  // Aguarda 2 milisegundos antes do próximo loop
  // para que o conversor analógico-digital estabilize
  // depois da última leitura
  delay(2);
}