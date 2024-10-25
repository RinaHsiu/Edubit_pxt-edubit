edubitRgbBit.show_rainbow()

def on_forever():
    edubitRgbBit.rotate_pixels(1)
    basic.pause(500)
basic.forever(on_forever)
