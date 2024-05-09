# Image Filter

The project can be reached at:

Voice: 416-779-9948  
Website: https://carleton.ca/sce/  
E-mail: yashkapoor@cmail.carleton.ca

## Description

This project contains a photo editing program, which allows the user to choose an image of their choice and apply specific filters to it cumulatively.  
The program is split up into two user interfaces: an interactive user interface and a batch user interface. The interactive user interface will allow  
the user to choose from a total of twelve commands, giving them the option to load an image, save the current image, apply a total of nine filters to  
the image and quit the program at any given time. On the other hand, the batch user interface will prompt the user to enter the name of a file, which  
will contain additional information to load an image, save an image to a designated folder and apply any of the nine filters to that image. 

The project is made up of four files:

T47_image_filters.py  
T47_interactive_ui.py  
T47_batch_ui.py  
T47_user_interface.py


## Installation
Must have windows 10 installed.
Python 3.7.4 or later must be installed. 
Python Image library, pip should be installed(iif not already installed with python). It can be done by typing the following into the command prompt.
```
bash
> pip install Pillow
```
Pip can be upgraded if need be by using the following command into the command prompt.
```
bash
> pip install --upgrade Pillow
```

An external library,[Cimpl.py](https://culearn.carleton.ca/moodle/pluginfile.php/3648678/mod_folder/content/0/Cimpl.py?forcedownload=1) which is a  
made-in-Carleton python library, must be downloaded to a folder.
The four files T47_image_filters.py,T47_interactive_ui.py,T47_batch_ui.py and T47_user_interface.py should be downloaded into the same folder where Cimpl.py is in.


## Usage
First, open T47_interactive_ui file then this will display.
```bash
L)oad Image   S)ave as
2)-tone       	3)-tone		X)treme contrast		T)int Sepia		P)osterizing
E)dge Detection        I)mproved Edge Detection	  	H)orizontal Flip	V)ertical Flip
Q)uit
```
Input in L or l in the python shell to load an image. A pop up window would show up asking to choose an image saved on the computer. Click on the desired image to load it.

Next, select what element you wish to run by typing the first letter in front of each element. For example: if you want (two-tone) then type 2 in the python shell. Then press enter, an edited image will show up.(if it doesn’t load click enter again). You must close the image to continue.
You may continue to enter any of the editing prompts until you end up with your desired product.
For example if you want a horizontal flipped image with Tint Sepia. Simply type ‘H’ or ’h’ in the shell then press enter, close the opened image then type”T” or “t” in the shell and hit enter. The overlay image with 2 effects will be shown.

In order to save the image, input “s” or ‘S’ on the python shell which will give a prompt asking for the directory for the file to be saved at. 
For exiting the program, input ‘q’ or ‘Q’ in the shell then type enter.

Useable buttons functions (can be CAPITAL or small)  
**L** - Load image  
**S** - Save image as  
**2** - Make image only has two tone(colors)  
**3** - Make image only has three tone(colors)  
**X** - Maximize the contrast between pixels  
**T** - Make Image yellowish like old picture  
**P** - Make image blurry    
**E** - creates an image that looks like a pencil sketch, by changing the pixels' colours to black or white. (need to enter the threshold value by typing a number and hitting enter)
(range of threshold value is 0-256)  
**I** - Improved version of above (pencil sketch) by comparing between each pixel and the 
pixel below it as well as the pixel to the right of it.(need to enter the threshold value by typing a number and hitting enter)
(range of threshold value is 0-256)    
**H** - Flip the image based on horizontal axis  
**V** - Flip the image based on vertical axis  
**Q** - Exit program

Example of load  horizontal flipped image with Tint Sepia then save.  
`>>>L`  
`>>>H`  
`>>>T`  
`>>>S`  
`>>>Q`

## Credits
- Yash Kapoor: Blue, Extreme Contrast and Improved Edge Detection Filter  
- Abraham Paulose: Green, Two-tone, Three-tone and Edge Detection Filter  
- Gordon Vanstokkom: Red, Sepia and Flip Vertical Filter  
- Ben Li: Combined, Posterizing and Flip Horizontal Filter

Copyright 2020. All rights reserved. 
