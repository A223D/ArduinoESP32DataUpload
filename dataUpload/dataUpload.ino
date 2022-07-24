#include "secrets.h"
#include <WiFi.h>

#define LED 2

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
  Serial.println("Let's begin by connecting to Wifi");
  WiFi.begin(WifiSSID, WifiPass);
  Serial.println("Waiting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  digitalWrite(2, HIGH);

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());


}

void loop() {
  delay(1000);


}
