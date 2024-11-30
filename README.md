Example of [WS2812-based LED matrix](https://cdn-shop.adafruit.com/datasheets/WS2812.pdf) with [MicroPython](https://micropython.org/) 

![Breadboard example](/breadboard.png)

## Hardware

- [8x8 LED Matrix](https://abra-electronics.com/opto-illumination/led-matrix/led-matrix-64-addressable-led-matrix-8-x-8.html)
- [ESP32 S3 Zero](https://www.waveshare.com/wiki/ESP32-S3-Zero)

## Test

```
mpremote run main.py
```

## Deploy

```
mpremote fs cp main.py :
```

## License

MIT
