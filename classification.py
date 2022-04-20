#!/usr/bin/python3
import jetson.inference
import jetson.utils

# Start the parser
import argparse
parser = argparse.ArgumentParser()
# googlenet
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
options = parser.parse_args()

# Start the camera
from jetcam.usb_camera import USBCamera
camera_width = camera_height = 224
camera = USBCamera(width=camera_width, height=camera_height, capture_width=640, capture_height=480, capture_device=0)

import time
def tprint(msg, delay):
    print(msg)
    time.sleep(delay)
def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')


clear()
for i in range(3,0,-1):
    tprint(f"Scanning in {i}s",1)
clear()
image = camera.read()

file_header = bytearray(f'P6\n{camera_width} {camera_height}\n255\n', 'ascii')
with open('scan.ppm', 'wb') as file:
    file.write(file_header)
    image.tofile(file)


scan = jetson.utils.loadImage('scan.ppm')
network = jetson.inference.imageNet(options.network)
ID, confidence = network.Classify(scan)
NAME = network.GetClassDesc(ID)

clear()
print(NAME,ID,str(confidence*100)[0:2]+"%")
RSVPs = [296]
if ID in RSVPs: print(f"Welcome to the party {NAME}!")
else: print(f"You were not invited!")
