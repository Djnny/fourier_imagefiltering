from PIL import Image
import sys


def pixel_data(path) -> list:
    """
    Extracts image data from the specified image as a list of (R,G,B,A) sets
    """
    image = Image.open(path, 'r')
    values = list(image.getdata())
    return values

balls = 'image.png'
stuff = pixel_data(balls)