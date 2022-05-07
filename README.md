### ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING WITH NVIDIA
#### Alex Barthel
---

# Artificially Intelligent Bouncer

This Bouncer AI was created as a simpler way for facial recognition and restriction of access. Bouncers are typically seen at parties that are whitelisted; although, there are people that act as bouncers, but they are in the military, at a government building, etc. This AI could be used to simplify access and increase the efficiency of identity verification.

![add image descrition here](direct image link here)

## The Algorithm

My program uses image detection to determine one face from another. The code works by importing the libraries USBCAMERA and CSICAMERA from jetcam. It determines whether you're using the USB or CSI camera, then enables the camera. Then it determines what categories it wants to collect data from such as person_0 and person_1. It then runs the following lines of code:<br>
`import ipywidgets
import traitlets
from IPython.display import display
from jetcam.utils import bgr8_to_jpeg`<br>
After that, it starts classifying the images. It uses `torch` and `torchvision` to train the model, and resnet-18 as the base for my custom network. I then use live video feed that is sent to the classifier to determine if it's one person or another.

## Running this project

1. ssh into your nano
2. Type: `./docker_dli_run.sh`
3. Once you are in your docker, type: `cd classification`
4. Type: `wget https://github.com/AlexBarthel/nvidia_project/blob/7dda3a857d86bbff0056b56e20a6481ab8e05300/final_project.ipynb`
5. Type: `cd` to navigate back to your home directory in the docker
6. Type: `cd data/classification`
7. Type: `wget https://github.com/AlexBarthel/nvidia_project/blob/21fb203891be6096e260d290c008a5e8f371533f/final_project.pth`
8. Open JupyterLab using the link it gave you when you started the docker.
9. Type the password `dlinano` when prompted
10. Once you are in JupyterLab on the left-hand side you will see a folder labeled `classification`. Click into that
11. Click on the file labeled `final_project.ipynb`
12. Run all of the code cells by pressing `CONTROL+ENTER` (Windows), `COMMAND+ENTER` (Mac).
13. Once you run code cell 7 wait for the interactive display to appear.
14. Navigate to the section circled in red, remove all the text in that box, and paste this: `/nvdli-nano/data/classification/final_project.pth`
![image](https://user-images.githubusercontent.com/98185865/167229715-9547b287-c4fd-42ef-8412-9e7f858241ce.png)
15. Click the button below labeled `load model`
16. Focus your camera so that your hair touches the top of the screen, and your chin touches the bottom.
17. Click the button labeled `evaluate`
18. In the section circled in red, you should see the sliders changing to say `real_alex 1.0` or `fake_alex 1.0`.
###### This model was trained to work with my face but sometimes it will work for other people. It seems to mostly go off of skin tone, but I managed to train my model to pretty much 100% accuracy.
![image](https://user-images.githubusercontent.com/98185865/167230010-88a26ef8-871c-49a1-a36f-1b236abecb07.png)

[View a video explanation here](video link)

---

# ! NOTICE !

This repository has been reworked to accomodate my project. My original version on VSCode had too many technical challenges that wasted my time and got me nowhere. The ipynb file and model export here are from me recreating my project in jupyterlab. I hope that this does not cause too much confusion and this is the reason why there are so many commits and file deletions on this repository.
