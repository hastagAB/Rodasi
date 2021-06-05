import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
%matplotlib inline
pip install keras-segmentation
from keras_segmentation.models.unet import resnet50_unet
import pickle


from PIL import Image
import matplotlib.pyplot as plt
%matplotlib inline

original_image = "dataset/semantic_drone_dataset/original_images/001.jpg"
label_image_semantic = "dataset/semantic_drone_dataset/label_images_semantic/001.png"

fig, axs = plt.subplots(1,2, figsize=(16, 8), constrained_layout=True)

axs[0].imshow( Image.open(original_image))
# axs.grid(False)

label_image_semantic = Image.open(label_image_semantic)
axs[1].imshow( Image.open(original_image))
# label_image_semantic = np.asarray(label_image_semantic)
axs[1].imshow(label_image_semantic,alpha = 0.6)
# axs[1].grid(False)

n_classes = 23 # Aerial Semantic Segmentation Drone Dataset tree, gras, other vegetation, dirt, gravel, rocks, water, paved area, pool, person, dog, car, bicycle, roof, wall, fence, fence-pole, window, door, obstacle
model = resnet50_unet(n_classes=n_classes ,  input_height=416, input_width=608  )
epochs = 10
model.train( 
    train_images =  "dataset/semantic_drone_dataset/original_images/",
    train_annotations = "dataset/semantic_drone_dataset/label_images_semantic/",
    checkpoints_path = "resnet50_unet" , epochs=epochs)


import time
from PIL import Image
import matplotlib.pyplot as plt
%matplotlib inline

start = time.time()

input_image = "dataset/semantic_drone_dataset/original_images/001.jpg"
out = model.predict_segmentation(
    inp=input_image,
    out_fname="out.png"
)

fig, axs = plt.subplots(1, 2, figsize=(20, 20), constrained_layout=True)

img_orig = Image.open(input_image)
axs[0].imshow(img_orig)
axs[0].set_title('Pridiction')
axs[0].grid(False)
axs[0].imshow(out,alpha = 0.6)


validation_image = "dataset/semantic_drone_dataset/label_images_semantic/001.png"

axs[1].imshow(img_orig)
axs[1].imshow( Image.open(validation_image),alpha = 0.6)
axs[1].set_title('Original')
axs[1].grid(False)

done = time.time()
elapsed = done - start


filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))