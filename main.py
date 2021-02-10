import numpy as np 
import cv2 
import json
from cv2 import cv2
from matplotlib import pyplot as plt 


path = '/home/hastagab/Desktop/TrackGreen/Example/ab.png'

  
def getStats(path):

  # Image operation using thresholding 
  img = cv2.imread(path) 
    
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
  ret, thresh = cv2.threshold(gray, 0, 255, 
                              cv2.THRESH_BINARY_INV +
                              cv2.THRESH_OTSU) 
  cv2.imshow('image', thresh) 

  kernel = np.ones((3, 3), np.uint8) 
  closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, 
                kernel, iterations = 2) 
  bg = cv2.dilate(closing, kernel, iterations = 1) 
  dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
  ret, fg = cv2.threshold(dist_transform, 0.02
              * dist_transform.max(), 255, 0) 
  cv2.imwrite('/home/hastagab/Desktop/TrackGreen/Example/abcd.png', fg)

  from PIL import Image
  im = Image.open('/home/hastagab/Desktop/TrackGreen/Example/abcd.png')

  image = cv2.imread('/home/hastagab/Desktop/TrackGreen/Example/abcd.png',0)
  count = cv2.countNonZero(image)  #Black Pixel count
  white_pix = (image.size-count)/(25.75/3)

  # print("Pixel count of trees : " + str(white_pix))
  # print("Total Pixel count : " + str(image.size))

  total_area = 912*912
  area_by_trees = total_area * ((white_pix) / image.size)

  # print("Total captured area : " + str(total_area) + " sq m")
  # print("Total area covered by trees : " + str(int(area_by_trees)) + " sq m")
  # print("Approximate number of trees : " + str(int(area_by_trees/25.75)))

  O2_seg = int(area_by_trees/25.75)*21772.43

  # print("O2 Segregation per annum : " + str(O2_seg) + " cubic-cm")

  x = {
    "pix_trees": white_pix,
    "pix_total": image.size,
    "total_area": total_area,
    "trees_area": area_by_trees,
    "trees_count": area_by_trees/25.75,
    "o2_seg": O2_seg
  }

  y = json.dumps(x)

  return y


print(getStats(path))