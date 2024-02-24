#include <Arduino.h>
#include "Adafruit_NeoPixel.h"

#define STRIP_FRONT_LEFT 6
#define STRIP_RIGHT_TOP 7

#define LED_COUNT 150 // leds per matrix

#define X 15
#define Y 15

#define FPS 10


enum class Side { FRONT, LEFT, TOP, RIGHT };

#define BLANK Adafruit_NeoPixel::Color(0, 0, 0)
#define GREEN Adafruit_NeoPixel::Color(0, 255, 0)
#define BLUE Adafruit_NeoPixel::Color(0, 0, 255)
#define RED Adafruit_NeoPixel::Color(255, 0, 0)

class Visualization
{
public:

  Visualization()
  {
    front_left.begin();
    right_top.begin();

    front_left.setBrightness(255);
    right_top.setBrightness(255);
  }

  /**
    draws a pixel on the 4-sided cube
  **/
  int drawPixel(Side side, int x, int y, uint32_t color)
  {
    int i; // strip index

    if (side == Side::FRONT) 
    {
        if(y % 2 == 0) // ->
        {
          i = x + (y * X) + (X * (y + 1));
        }
        else // <-
        {
          i = (y * X) + (X * (y + 1)) - 1 - x;
        }
    }
    else if (side == Side::LEFT) 
    {
        if(y % 2 == 0) // ->
        {
          i = x + (y * X * 2);
        }
        else          // <-
        {
          i = (X - x - 1) + (y * (X * 2) + X);
        }
    }
    else if (side == Side::RIGHT) 
    {
      // right_top
    }
    else if (side == Side::TOP) 
    {
      // right_top
    }
    Serial.println(i);
    return -1;
  }

private:

  Adafruit_NeoPixel front_left = Adafruit_NeoPixel(LED_COUNT, STRIP_FRONT_LEFT, NEO_GRB + NEO_KHZ800);
  Adafruit_NeoPixel right_top = Adafruit_NeoPixel(LED_COUNT, STRIP_RIGHT_TOP, NEO_GRB + NEO_KHZ800);
};