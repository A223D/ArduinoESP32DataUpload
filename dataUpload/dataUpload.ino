#include "secrets.h"
#include <WiFi.h>
#define LED 2

int toggleMe = 0;
const char* host = "database.deta.sh";

WiFiClient client;

void setup() {
  Serial.begin(115200);
  char* testConcat = (char *)malloc((strlen("/v1/") + strlen(detaID) + strlen("/") + strlen(detaBaseName) + strlen("/") + strlen("items") + 1 )*sizeof(char));
  strcpy(testConcat, "/v1/");
  strncat(testConcat, detaID, strlen(detaID));
  strncat(testConcat, "/", strlen("/"));
  strncat(testConcat, detaBaseName, strlen(detaBaseName));
  strncat(testConcat, "/", strlen("/"));
  strncat(testConcat, "items", strlen("items"));
  Serial.println(testConcat);
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
}

void loop() {
    
  
  //if(!client.connect("
  

}
