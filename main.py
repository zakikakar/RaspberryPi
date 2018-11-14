from sense_hat import SenseHat
sense = SenseHat()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
navn = "ZAKI"

while True:
  sense.show_message(navn, scroll_speed=0.1, text_colour=yellow, back_colour=blue)
  sense.clear(red)