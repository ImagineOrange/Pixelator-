#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 02:27:11 2020

@author: ethancrouse
"""
from PIL import Image
import time
import sys

def main(): #prompts for image file and prints stats
    try: 
        print("\nThis script pixelates images. Enter information in the fields below: ")
        path = str(input("Image File Path: "))
        image = Image.open(path)
        print("\nImage information: ", image.format, image.size, image.mode) #display img info 
        level = int(input("Enter Pixelation level. 1-5: "))
    
    except FileNotFoundError:
        er=input("Error, file not found.\nWould you like to try again? (Y/N): ")
        if not er == 'Y':
            sys.exit
        else:
            main()
        
    LVL = 0   

    if level == 1 : 
        LVL= .05
    elif level ==2 : 
        LVL= .04
    elif level == 3 :        #establishes pixelation level
        LVL = .03
    elif level == 4 :
        LVL = .02
    elif level == 5 :
        LVL = .01
    else: 
        print("Error, invalid input. Restarting program.")
        main()
    image = Image.open(path)
    print("\nPixelizing image...")
    time.sleep(2)
    pixelizer(image,LVL)

def pixelizer(img,LVL): #resizes pixel with bilinear interpolation 
    xpixel,ypixel = img.size[0],img.size[1]
    xpixel = int(xpixel*LVL)
    ypixel = int(ypixel*LVL)
    reform = img.resize((xpixel,ypixel),resample=Image.BILINEAR) #grid to be used !!!
    reform.save('TEMP.JPG')
    pixel = reform.resize(img.size,Image.NEAREST) #image resized to original image resolution 
    pixel.show()
    again = input("\nType 'Y' to pixelate again. Type 'N' to exit program. Otherwise, type 'save' to save the pixelated image. ")
    if again == 'N':
        print("\nThank you!")
        pixel.close()
        sys.exit()
    elif again == 'Y':
        print('\n******************************\n')
        main()
    elif again == 'save':
        saver(pixel)
    else:
        print("Error, invalid input. Restarting program.")


def saver(pixel):
    filename = input('Save image as: ')
    pixel.save(filename)
    again = input("\nType 'Y' to pixelate again. Type 'N' to exit program. ")
    if again == 'N':
        print("\nThank you!")
        pixel.close()
        sys.exit()
    elif again == 'Y':
        print('\n******************************\n')
        main()

main()

