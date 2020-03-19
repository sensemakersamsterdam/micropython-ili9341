# test of printing multiple fonts to the ILI9341 on an M5Stack using H/W SP
# MIT License; Copyright (c) 2017 Jeffrey N. Magee
#
# Adapted for Sensemakers. Changed pins for the TTGO T4-V1.3 board
from ili934xnew import ILI9341, color565
from machine import Pin, SPI, PWM
import glcdfont
import tt14
import tt24
import tt32
from time import sleep

fonts = [glcdfont,tt14,tt24,tt32]
colors = [color565(255,0,0), color565(0,255,0),color565(0,0,255),color565(150,150,0)]

text = 'Now is the time for all Sensemakers to come to the aid of the party.'

spi = SPI(
    2,
    baudrate=30000000,
    miso=Pin(12),
    mosi=Pin(23),
    sck=Pin(18))

display = ILI9341(
    spi,
    cs=Pin(27),
    dc=Pin(32),
    rst=Pin(5),
    w=320,
    h=240,
    r=3)

display.erase()
display.set_pos(0,0)

bg_led = PWM(Pin(4))
bg_led.freq(1000)
bg_led.duty(750)

for ff,col in zip(fonts,colors):
    display.set_color(col,0)
    display.set_font(ff)
    display.print(text)

while True:
    lum = 0
    for _ in range(5):
        lum += 200
        bg_led.duty(lum)
        sleep(2)

