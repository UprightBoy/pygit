#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def rndChar():
    return chr(random.randint(65, 90))


def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width, height = 60 * 4, 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 48)
darw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        darw.point((x, y), fill=rndColor1())
for t in range(4):
    darw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('VerficationCode.jpg', 'jpeg')
