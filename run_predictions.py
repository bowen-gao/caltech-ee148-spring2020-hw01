import os
import numpy as np
import json
from PIL import Image, ImageDraw


def detect_red_light(I):
    '''
    This function takes a numpy array <I> and returns a list <bounding_boxes>.
    The list <bounding_boxes> should have one element for each red light in the 
    image. Each element of <bounding_boxes> should itself be a list, containing 
    four integers that specify a bounding box: the row and column index of the 
    top left corner and the row and column index of the bottom right corner (in
    that order). See the code below for an example.
    
    Note that PIL loads images in RGB order, so:
    I[:,:,0] is the red channel
    I[:,:,1] is the green channel
    I[:,:,2] is the blue channel
    '''

    bounding_boxes = []  # This should be a list of lists, each of length 4. See format example below.

    '''
    BEGIN YOUR CODE
    '''
    kernel1 = Image.open("kernel1.jpg")
    kernel1 = np.asarray(kernel1)
    kernel2 = Image.open("kernel2.jpg")
    kernel2 = np.asarray(kernel2)
    kernel3 = Image.open("kernel3.jpg")
    kernel3 = np.asarray(kernel3)
    kernel4 = Image.open("kernel4.jpg")
    kernel4 = np.asarray(kernel4)
    kernel5 = Image.open("kernel5.jpg")
    kernel5 = np.asarray(kernel5)
    kernels = [kernel1, kernel3, kernel4, kernel5]
    for kernel in kernels:
        box_height = kernel.shape[0]
        box_width = kernel.shape[1]
        img_height = I.shape[0]
        img_width = I.shape[1]
        kernel_vector = np.reshape(kernel, box_width * box_height * 3) / 127.5 - 1
        for h in range(0, img_height - box_height, 1):
            for w in range(0, img_width - box_width, 1):
                cur_box = I[h:h + box_height, w:w + box_width, :] / 127.5 - 1
                cur_box = np.reshape(cur_box, box_width * box_height * 3)
                # arc cosine between two vectors
                value = np.dot(cur_box, kernel_vector) / (np.linalg.norm(cur_box) * np.linalg.norm(kernel_vector))
                # if the value larger than a threshold
                if value > 0.93:
                    bounding_boxes.append([h, w, h + box_height, w + box_width])

    '''
    END YOUR CODE
    '''

    for i in range(len(bounding_boxes)):
        assert len(bounding_boxes[i]) == 4

    return bounding_boxes


# set the path to the downloaded data:
data_path = 'RedLights2011_Medium'

# set a path for saving predictions: 
preds_path = 'hw01_preds'
os.makedirs(preds_path, exist_ok=True)  # create directory if needed

# get sorted list of files: 
file_names = sorted(os.listdir(data_path))

# remove any non-JPEG files: 
file_names = [f for f in file_names if '.jpg' in f]

preds = {}

for i in range(333, len(file_names)):
    # read image using PIL:
    I = Image.open(os.path.join(data_path, file_names[i]))

    # convert to numpy array:
    I = np.asarray(I)

    preds[file_names[i]] = detect_red_light(I)
    im = Image.open(os.path.join(data_path, file_names[i]))
    draw = ImageDraw.Draw(im)
    for box in preds[file_names[i]]:
        draw.rectangle([box[1], box[0], box[3], box[2]])
    im.show()
    print(preds[file_names[i]])
    break
# save preds (overwrites any previous predictions!)
with open(os.path.join(preds_path, 'preds.json'), 'w') as f:
    json.dump(preds, f)
