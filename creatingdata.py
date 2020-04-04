"""
from PIL import Image
import csv

im = Image.open('InfectedLeaves/IMG_2688.jpg') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
print(pix[0,0])  # Get the RGBA Value of the a pixel of an image
print("Hi")
print(im.getdata())
with open('training_data.csv', mode='w') as training_file:
    training_writer = csv.writer(training_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    training_writer.writerow(['John Smith', 'Accounting', 'November'])
    training_writer.writerow(['Erica Meyers', 'IT', 'March'])
"""
from PIL import Image
import numpy as np
import sys
import os
import csv

#Useful function
def createFileList(myDir, format='.JPG'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# load the original image
myFileList = createFileList('/Users/marcriccione/Desktop/CSCE421/ENDEAVRML/InfectedLeavesTrain/')
myFileList2 = createFileList('/Users/marcriccione/Desktop/CSCE421/ENDEAVRML/NotInfectedLeavesTrain/')
myFileList3 = createFileList('/Users/marcriccione/Desktop/CSCE421/ENDEAVRML/InfectedLeavesTest/')
myFileList4 = createFileList('/Users/marcriccione/Desktop/CSCE421/ENDEAVRML/NotInfectedLeavesTest/')

# create a writer that is of type dict writer for training
fnamesTrain = ['infected', 'pixels']
pixel_string = ''
f = open("training_pixels.csv", 'w')
writer = csv.DictWriter(f,fieldnames=fnamesTrain)
writer.writerow({'infected' : 'infected', 'pixels' : 'pixels'})

for file in myFileList:
    #print(file)
    shrink = (100,100)
    img_file = Image.open(file)
    # img_file.show()
    # get original image parameters...
    img_file = img_file.resize(shrink)
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    value = value.tolist()
    for i in range(len(value)):
      pixel_string = pixel_string + str(value[i]) + ' '
    #print(pixel_string)
    writer.writerow({'infected' : '1', 'pixels' : pixel_string})
    pixel_string = ''

for file in myFileList2:
    #print(file)
    shrink = (100,100)
    img_file = Image.open(file)
    # img_file.show()
    # get original image parameters...
    img_file = img_file.resize(shrink)
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    value = value.tolist()
    for i in range(len(value)):
      pixel_string = pixel_string + str(value[i]) + ' '
    #print(pixel_string)
    writer.writerow({'infected' : '0', 'pixels' : pixel_string})
    pixel_string = ''

f = open("test_pixels.csv", 'w')
writer = csv.DictWriter(f,fieldnames=fnamesTrain)
writer.writerow({'infected' : 'infected', 'pixels' : 'pixels'})

for file in myFileList3:
    #print(file)
    shrink = (100,100)
    img_file = Image.open(file)
    # img_file.show()
    # get original image parameters...
    img_file = img_file.resize(shrink)
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    value = value.tolist()
    for i in range(len(value)):
      pixel_string = pixel_string + str(value[i]) + ' '
    #print(pixel_string)
    writer.writerow({'infected' : '1', 'pixels' : pixel_string})
    pixel_string = ''

for file in myFileList4:
    #print(file)
    shrink = (100,100)
    img_file = Image.open(file)
    # img_file.show()
    # get original image parameters...
    img_file = img_file.resize(shrink)
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    value = value.tolist()
    for i in range(len(value)):
      pixel_string = pixel_string + str(value[i]) + ' '
    #print(pixel_string)
    writer.writerow({'infected' : '0', 'pixels' : pixel_string})
    pixel_string = ''