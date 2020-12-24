#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 02:27:11 2020

@author: ethancrouse
"""
import easygui as g
from PIL import Image
import sys
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import pyplot as plt
# import numpy as np
# from colorthief import ColorThief


def main(): #prompts for image file and prints stats

    msg = "Enter information in the fields below: "
    title = "Pixelator: Image Selection"
    fieldnames = ["Image File Path: "]
    fieldvalue = []
    fieldvalue  = g.multenterbox(msg,title,fieldnames)
    if fieldvalue == ' ':
        print("Error")
    else:
        pass
    file=fieldvalue[0]
    image = Image.open(file)
    print("Image information: ", image.format, image.size, image.mode)
    pixelizer(image)


def pixelizer(img): #resizes pixel with bilinear interpolation 
    
    msg = "Enter Pixel dimensions: "
    title = "Pixelator: Pixel dimensions"
    fieldnames = ["Give the desired x dimension pixel length: ", "Give the desired y dimension pixel length: "]
    x_by_y = []
    x_by_y = g.multenterbox(msg,title,fieldnames)
    x_pixel,y_pixel = int(x_by_y[0]),int(x_by_y[1])

    reform = img.resize((x_pixel,y_pixel),resample=Image.BILINEAR) #grid to be used !!!
    reform.save('TEMP.JPG')
    pixel = reform.resize(img.size,Image.NEAREST) #image resized to og size
    pixel.show()

    
    
    
main()
sys.exit(0)

#create a constant for pixel resizing
#show relevant pixel dimensions in popup window 
#save pixel photo in folder 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Extra functionality 
    # weights(reform,number_pixels)


# def weights(img,n): #capture RGB values from each pixel in image
#     color_thief = ColorThief('TEMP.JPG')
#     colors = color_thief.get_palette(color_count=256) #returns pallet of 256 average colors
#     values=[]
#     for i in range (len(colors)):
#         if colors[i] != (100,100,120):  # PRINTS A LIST OF PALETTED COLORS IN RGB 
#             values.append(colors[i])
#         else:
#             pass
    
#     fig = plt.figure()
#     axis = fig.add_subplot(1, 1, 1, projection="3d") # 3D plot with scalar values in each axis
    
#     im = Image.open('TEMP.JPEG')
#     r, g, b = list(im.getdata(0)), list(im.getdata(1)), list(im.getdata(2))

#     axis.scatter(r, g, b, c="#ff0000", marker="o")
#     axis.set_xlabel("Red")
#     axis.set_ylabel("Green")
#     axis.set_zlabel("Blue")
#     plt.show()
    
  
   
#     # numpy_array = np.array(pixels)
#     # RGBs=[]
#     # print(numpy_array.shape)
#     # for i in range (len(numpy_array)):
#     #     for j in range(1,len(numpy_array[i])):
#     #         RGBs.append(numpy_array[j])
        
#     # print(RGBs)
#     # print()
#     # print(len(RGBs))
        
    

# main(
#      )