from PIL import Image
im = Image.open('download.jpeg')

green = 0
other = 0

for pixel in im.getdata():
    if pixel == (124,252,0) : 
        green += 1
    elif pixel == (127,255,0) :
        green += 1
    elif pixel == (50,205,50) :
        green += 1
    elif pixel == (0,255,0) :
        green += 1
    else:
        other += 1
print('green=' + str(green)+', other='+str(other))
