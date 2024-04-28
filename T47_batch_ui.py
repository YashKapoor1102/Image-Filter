""" 
ECOR 1051 Winter 2020
Project Milestone 3

Created by Team 47
Members: Yash Kapoor: 101163338 (Team Leader), Gordon Vanstokkom: 100980313, Abraham Paulose: 101168299 and Ben Li: 101113284
on March 30th, 2020
to create a batch user interface that allows the user to apply different filters to an image

Date of Submission: April 2nd, 2020
"""

from T47_image_filters import *
from T47_user_interface import *

#Code was refactored and documented by Yash Kapoor and Gordon Vanstokkom

def user_filename_input() -> None:
    
    """
    Created by Yash Kapoor
    
    Allows the user to input a filename 

    """    
    
    global filename
    
    filename = input("\nPlease enter a filename: ")
    #prompting the user for a filename that ends with .txt
    

def get_each_line_and_filter() -> None:
    
    """
    Created by Yash Kapoor and Gordon Vanstokkom
    
    Stores each word in a single line of the .txt file into a list and gets every single filter applied to the image
    chosen by the user 
    
    """
    
    infile = open(filename, 'r')    
    
    for line in infile:
    #for loop used to get every single line one by one in the .txt file chosen by the user
        
        global set_of_lines
        
        set_of_lines = line.split()
        #splitting every word in a line and storing those individual words into a list 
        
        global image
        
        image = load_image(set_of_lines[0])
        #loading the image that is written in the .txt file    
        
        for image_filter in set_of_lines[2:]:
        #for loop used to get every single filter applied to the loaded image in the .txt file
            
            if image_filter == "2":
        
                colors = colors_two_tone()
        
                image = two_tone(image, colors[0], colors[1])
                
        
            elif image_filter == "3":
        
                colors = colors_three_tone()
        
                image = three_tone(image, colors[0], colors[1], colors[2])
            
        
            elif (image_filter == "X") or (image_filter == "x"):
        
                image = extreme_contrast(image)
                
        
            elif (image_filter == "T") or (image_filter == "t"):
        
                image = sepia(image)
            
        
            elif (image_filter == "P") or (image_filter == "p"):
        
                image = posterizing(image)
        
                
            elif (image_filter == "E") or (image_filter == "e"):
        
                image = detect_edges(image, 10)
                
        
            elif (image_filter == "I") or (image_filter == "i"):
        
                image = detect_edges_better(image, 10)
        
        
            elif (image_filter == "H") or (image_filter == "h"):
        
                image = flip_horizontal(image)
        
            else:
                
                #This is to flip an image vertically
                image = flip_vertical(image)
                            
        
        save_image_into_folder = save_image()
        #saving the image as the name that is specified in the .txt file by the user    
        
    infile.close()

def save_image() -> None:
    
    """
    Created by Gordon Vanstokkom
    
    Saves the image into the folder that has the name that is specified in the .txt file
    
    """
    
    save_as(image, set_of_lines[1])



#Main Script

if __name__ == "__main__":
    
    user_prompt_filename = user_filename_input()

    filter_applied_to_image = get_each_line_and_filter()



    
    


 