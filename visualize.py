import os
import numpy as np
import json
from PIL import Image, ImageDraw

f = open('hw01_preds/preds.json')

preds = json.load(f)
lis = []
for filename in preds:
    I = Image.open("RedLights2011_Medium/" + filename)
    I.show()
    draw = ImageDraw.Draw(I)
    for box in preds[filename]:
        draw.rectangle([box[1], box[0], box[3], box[2]])
    I.show()
    I.save("hw01_visualizations/" + filename)
