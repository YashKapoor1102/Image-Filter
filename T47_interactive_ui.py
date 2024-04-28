""" 
ECOR 1051 Winter 2020
Project Milestone 3

Created by Team 47
Members: Yash Kapoor: 101163338 (Team Leader), Gordon Vanstokkom: 100980313, Abraham Paulose: 101168299 and Ben Li: 101113284
on March 29th, 2020
to create a user interface that allows the user to load an image and apply different filters to it 

Date of Submission: April 2nd, 2020
"""

from T47_image_filters import *
from T47_user_interface import *

#Code was refactored and documented by Abraham Paulose and Ben Li
def menu_of_commands() -> str: 
    
    """
    Created by Abraham Paulose
    
    Returns a string that outlines the set of commands which the user can enter 
    
    """
    
    #Declaring a variable that contains all the menu commands available in the photo-editing program
    program_menu_commands = (
            "\nL)oad image\tS)ave as\n2)-tone\t\t3)-tone\t\tX)treme contrast\tT)int Sepia\t\tP)osterizing\nE)dge Detection\t\tI)mproved Edge Detection\tH)orizontal Flip\tV)ertical Flip\nQ)uit\n\n: ")   
    
    return program_menu_commands

def user_input() -> str:
    
    """
    Created by Ben Li
    
    Returns a string which contains the letters/numbers entered by the user
    
    """
    
    global user_filter_choice
    
    user_filter_choice = input(menu_of_commands()).lower()
    
    return user_filter_choice

def threshold_chosen() -> int:
    
    """
    Created by Abraham Paulose
    
    Returns an integer that is the threshold value chosen by the user
    
    """
    threshold = int(input("\nPlease enter a threshold value: "))
    
    return threshold
    
def load_save_image() -> None:  
    
    """
    Created by Abraham Paulose
    
    Contains three commands out of twelve commands in total and checks to see if the user has entered any of these commands.
    
    """
    
    if user_filter_choice == "l":
    
        load_save_image.image = load_image(choose_file()) 
        
        show(load_save_image.image)
        #Loads an image that is chosen by the user and displays it to the user

    
    elif user_filter_choice == "q":
            
        print("\nThank you for trying out this program!")
            
    else:
    
        save_as(load_save_image.image)   
        
def first_set_image_filters() -> None:  
    
    """
    Created by Yash Kapoor
    
    Contains three image filters out of eight image filters in total and checks to see if the user has entered any of these
    image filters.
    
    """
    if user_filter_choice == "2":

        colors = colors_two_tone()

        load_save_image.image = two_tone(load_save_image.image, colors[0], colors[1])
        show(load_save_image.image)
        
    elif user_filter_choice == "3":
    
        colors = colors_three_tone()

        load_save_image.image = three_tone(load_save_image.image, colors[0], colors[1], colors[2])
        show(load_save_image.image)

    else:
    
        load_save_image.image = extreme_contrast(load_save_image.image)
        show(load_save_image.image)


def second_set_image_filters() -> None:
    
    """
    Created by Yash Kapoor
    
    Contains three more image filters out of eight image filters in total and checks to see if the user has entered
    any of these image filters.
    
    """
    
    if user_filter_choice == "t":

        load_save_image.image = sepia(load_save_image.image)
        show(load_save_image.image)

    elif user_filter_choice == "e":
        
        try:
            
            #prompting the user for a threshold value for the edge detection filter
            threshold = threshold_chosen()
    
            load_save_image.image = detect_edges(load_save_image.image, threshold)
            show(load_save_image.image)
            
        except:
            
            print("\nYou must enter a valid threshold value. Try again and ensure you have loaded an image!") 
            
    else:
        
        load_save_image.image = posterizing(load_save_image.image)   
        show(load_save_image.image)
            
def third_set_image_filters() -> None:
    
    """
    Created by Yash Kapoor
    
    Contains the last three image filters out of eight image filters in total and checks to see if the user has entered
    any of these image filters.
    
    """
    
    if user_filter_choice == "i":
            
        try:
                
            #prompting the user for a threshold value for the improved edge detection filter
            threshold = threshold_chosen()
                
            load_save_image.image = detect_edges_better(load_save_image.image, threshold)
            show(load_save_image.image)
                
        except:
                
            print("\nYou must enter a valid threshold value. Try again and ensure you have loaded an image!")
            
            
    elif user_filter_choice == "h":
        
        load_save_image.image = flip_horizontal(load_save_image.image)
        show(load_save_image.image)
        
    else:
        
        load_save_image.image = flip_vertical(load_save_image.image)   
        show(load_save_image.image)

def displayed_image() -> None:
    
    """
    Created by Yash Kapoor
    
    Contains a list of all the commands, which can be chosen by the user, and adds funtionality to each command
    that the user can choose. If the user chooses to apply a specific filter to the image, it displays that image
    to the user after that filter has been applied to it.
    
    """
    
    user_filter_choice = ""  #Declaring a variable and storing an empty string value in it to use in the while loop


    # This while loop below is created by Yash Kapoor by combining everyone's main script together to make it more organized
    
    while (user_filter_choice != "Q") and (user_filter_choice != "q"):
    #As long as the user does not input "Q" or "q", all the code below will keep executing
        
        user_filter_choice = user_input()        
        
        first_commands_list = ["q", "l", "s"]
        #first set of commands stored in a list 
        
        second_commands_list = ["2", "3", "X", "x"]
        third_commands_list = ["T", "E", "P", "t", "e", "p"]
        
        #second and third set of commands stored in a list
        
        
        commands_list = ["q", "l", "s", "2", "3", "x", "t", "e", "p", "i", "h", "v"] 
        #full list of commands that the user is able to choose from, when they run the program
        
        try:
        #If an error is found in the "try" block, the code inside the "except" block will execute instead
            
            if user_filter_choice not in commands_list:
                
                print("\nNo such command! Try again!")              
            
            elif user_filter_choice in first_commands_list:
                
                first_set_of_commands = load_save_image()
            
                
            elif user_filter_choice in second_commands_list:
                
                second_set_of_commands = first_set_image_filters()
                
            elif user_filter_choice in third_commands_list:
                
                third_set_of_commands = second_set_image_filters()
                
            else:
                
                fourth_set_of_commands = third_set_image_filters()

        except:
            
            print("\nNo image loaded! You must load an image first.")    
    
#Main Script

if __name__ == "__main__":
    
    filter_applied_to_image = displayed_image()