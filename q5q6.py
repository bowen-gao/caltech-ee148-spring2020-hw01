import json
from PIL import Image, ImageDraw

f = open('hw01_preds/preds.json')

preds = json.load(f)

# code for question 5

# here are some images that my algorithm succeeded
good_images = ["RL-036.jpg", "RL-048.jpg", "RL-332.jpg"]

for image in good_images:
    I = Image.open("RedLights2011_Medium/" + image)
    draw = ImageDraw.Draw(I)
    for box in preds[image]:
        draw.rectangle([box[1], box[0], box[3], box[2]])
    I.show()

# here are some images that my algorithm failed
bad_images = ["RL-334.jpg", "RL-167.jpg", "RL-163.jpg"]

for image in bad_images:
    I = Image.open("RedLights2011_Medium/" + image)
    draw = ImageDraw.Draw(I)
    for box in preds[image]:
        draw.rectangle([box[1], box[0], box[3], box[2]])
    I.show()

# code for q6

# here is one example that shows one potential problem of my approach:

I = Image.open("RedLights2011_Medium/RL-001.jpg")
draw = ImageDraw.Draw(I)
for box in preds["RL-001.jpg"]:
    draw.rectangle([box[1], box[0], box[3], box[2]])
I.show()
