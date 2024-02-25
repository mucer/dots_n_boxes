#include <Adafruit_NeoPixel.h>
#include "GameLogic.cpp"
#define PIN        6
#define NUMPIXELS 300 // Popular NeoPixel ring size

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

#define DELAYVAL 1000

GameLogic gameLogic;

void setup() {
  pixels.begin();
  Serial.begin(9600);
  Serial.println("setup");
}

void loop() {
  // pixels.clear(); // Set all pixel colors to 'off'

  gameLogic.tick();

  delay(DELAYVAL); // Pause before next pass through loop
}