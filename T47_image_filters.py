""" 
ECOR 1051 Winter 2020
Project Milestone 2

Created by Team 47
Members: Yash Kapoor: 101163338 (Team Leader), Gordon Vanstokkom: 100980313, Abraham Paulose: 101168299 and Ben Li: 101113284
on March 25th, 2020
to apply different filters to an image

"""

from Cimpl import *
from simple_Cimpl_filters import grayscale


# Blue colour filter
def color_filter(image: Image) -> Image:
    """
    Created by Yash Kapoor
    on March 8th, 2020 
    to apply a blue filter to an original image

    Return a blue copy of the image. Each pixel in the original image is turned to blue to display a
    blue copy of the image.
    
    >>> image = load_image(choose_file())
    >>> blue_image = color_filter(image)
    >>> show(blue_image)
    
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        
        new_color = create_color(0, 0, b)
        set_color(new_image, x, y, new_color)

    return new_image


# Green colour filter
def pic_to_green(filename: Image) -> Image:
    
    """
    Created by Abraham Paulose
    on March 8th, 2020 
    to apply a green filter to an original image

    Returns an image which is a copy of the original image filename but with all of its pixels retaining the colour green only.

    >>> image = load_image(choose_file())
    >>> green_image = pic_to_green(image)
    >>> show(green_image)

    
    """
    original_image = filename
    new_image = copy(original_image)  # Makes a copy of the original image
    
    for pixel in original_image:
        
        x, y, (r, g, b) = pixel
        new_colour = create_color(0, g, 0)  # r and b are set to zero except g in order to apply a green filter
        set_color(new_image, x, y, new_colour)

    return (new_image)


# Red colour filter
def red_channel(image: Image) -> Image:
    """
    Created by Gordon Vanstokkom
    on March 8th, 2020 
    to apply a red filter to an original image
    
    Return a redscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> red_image = red_channel(image)
    >>> show(red_image)
    
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        
        # Use the pixel's brightness as the value of R component for the
        # shade of Red. These means that the pixel's original colour and the
        # corresponding red shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        red = create_color(brightness, 0, 0)
        set_color(new_image, x, y, red)

    return new_image


# Combine filter
def add_color(color1: tuple,
              color2: tuple) -> list:  # add_color function Created by Ben Li to aid in creating a combined function
    # this is a helping function

    """
    Created by Ben Li
    on March 8th, 2020 
    
    Returns a new color that is the sum of the two existing colors 
    
    color1 is the first color gotten from the combined function
    color2 is the second color gotten from the combined function
    
    """

    tmp = []
    # storing an empty list in the variable called tmp

    # for loop created to add the two colors together until one less than the length of color1 is reached
    for i in range(len(color1)):
        
        tmp.append(color1[i] + color2[i])  # adding on the sum of two colors onto a list

    return create_color(*tmp)


def combine(red_image: Image, blue_image: Image,
            green_image: Image) -> Image:  # Combined filter function Created by Ben Li

    """
    Created by Ben Li
    on March 8th, 2020 
    to take three images (e.g., Red, Green and Blue Images) and produce an image by combining these three RGB values together
    
    Returns a combined image that combines the pixels of the red image, green image and blue image
    
    >>> combine(image_a, image_b, image_c) 
    each channel filter is separated and then combined to form a single image
    >>> show(image_combined)
    displays the new copy of a single image that has been combined by seperating three channel filters
    
    """
    combined_image = copy(red_image)
    # copying the image called red_image and storing it in the variable called combined_image

    # for loop created to combine the pixel values of red, blue and green images together to form a combined image
    for x, y, red_image_color in red_image:
        
        blue_image_color = get_color(blue_image, x, y)
        green_image_color = get_color(green_image, x, y)
        
        color = add_color(add_color(blue_image_color, green_image_color), red_image_color)
        
        set_color(combined_image, x, y, color)

    return combined_image


# The two tone filter function below is created by Abraham Paulose

#These are the list of colors that the user can choose to input
Colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'lime': (0, 255, 0), 'blue': (0, 0, 255),
          'yellow': (255, 255, 0), 'cyan': (0, 255, 255), 'magenta': (255, 0, 255), 'grey': (128, 128, 128)}


def two_tone(image: Image, first_colour: str, second_colour: str) -> Image:
    
    """
    Created by Abraham Paulose
    on March 13th, 2020
    
    Return a new copy of the original image with a two tone filter applied to it

    >>> image = load_image(choose_file())
    >>> new_image = two_tone(image,black,blue)
    >>> show(new_image)
    
    """

    new_image = copy(image)

    for pixel in new_image:

        x, y, (r, g, b) = pixel

        if 0 <= (r + g + b) / 3 <= 127:

            new_colour = create_color(*Colors[first_colour])
            set_color(new_image, x, y, new_colour)
            
        # If (r+g+b)/3 is in the 0-127 range, then the corresponding r,g,b values are taken from the key(first_colour) in the
        # Dictionary which is then created and set to the new_image
        
        else:

            new_colour = create_color(*Colors[second_colour])
            set_color(new_image, x, y, new_colour)
        # Else it is set to the value of the key , second_colour

    return new_image


# Three tone filter
def three_tone(image: Image, first_colour: str, second_colour: str, third_colour: str):
    
    """
    Created by Abraham Paulose
    on March 15th, 2020
    
    Return a new copy of the original image with a three tone filter applied to it

    >>> image = load_image(choose_file())
    >>> new_image = three_tone(image,black,blue,magenta)
    >>> show(new_image)
    
    """

    new_image = copy(image)

    for pixel in new_image:

        x, y, (r, g, b) = pixel

        if 0 <= (r + g + b) / 3 <= 84:

            new_colour = create_color(*Colors[first_colour])
            set_color(new_image, x, y, new_colour)
        # If (r+g+b)/3 is in the 0-84 range, then the corresponding r,g,b values are taken from the key(first_colour) in the
        # Dictionary which is then created and set to the new_image
        
        elif 85 <= (r + g + b) / 3 <= 170:

            new_colour = create_color(*Colors[second_colour])
            set_color(new_image, x, y, new_colour)
        # If (r+g+b)/3 is in the 85-170 range,then the corresponding r,g,b values are taken from the key(second_colour) in the
        # Dictionary which is then created and set to the new_image

        else:
            
            new_colour = create_color(*Colors[third_colour])
            set_color(new_image, x, y, new_colour)
        # Else it is set to the value of the key , third_colour

    return new_image


# Extreme contrast filter
def extreme_contrast(image: Image) -> Image:
    
    """
    Created by Yash Kapoor
    on March 14th, 2020
    to apply an extreme contrast filter to an image
    
    Return an image which has different red, green and blue components depending on the value of the image's original RGB components

    >>> image = load_image(choose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)

    """
    new_image = copy(image)
    # making a new copy of the original image

    for pixel in new_image:
        # using a for loop to get all the pixels of the selected image by the user

        x, y, [r, g, b] = pixel
        # assigning the values stored in 'pixel' into new variables.
        
        
        if 0 <= r <= 127:
            # if the red component of the pixel is between 0 and 127, the value of the red component will change to 0.

            r = 0

        else:
            # if the condition above is not satisfied, the value of the red component will change to 255.

            r = 255


        if 0 <= g <= 127:
            # if the green component of the pixel is between 0 and 127, the value of the green component will change to 0

            g = 0

        else:
            # if the condition above is not satisfied, the value of the green component will change to 255

            g = 255


        if 0 <= b <= 127:
            # if the blue component of the pixel is between 0 and 127, the value of the blue component will change to 0

            b = 0

        else:
            # if the condition above is not satisfied, the value of the blue component will change to 255
            b = 255

        new_color = create_color(r, g, b)
        # creating a new color with the new red, green and blue values and storing that new color in the variable called new_color

        set_color(new_image, x, y, new_color)
    # applying the new color to the image

    return new_image


# Sepia Image filter
def sepia(image: Image) -> Image:
    
    """
    Created by Gordon Vanstokkom (100980313)
    on March 16th, 2020
    to apply a sepia filter to an image
    
    Returns a sepia copy of the image.
   
    >>> image = load_image(choose_file())
    >>> new_image = sepia(image)
    >>> show(new_image)
    
    """
    new_image = copy(grayscale(image))

    for x, y, (r, g, b) in new_image:

        if r < 63: 
            
            new_blue = b * 0.9  # sets blue to 90% of original intensity
            new_red = r * 1.1  # sets red to 110% of original intensity
            
            sepia = create_color(new_red, g, new_blue)  # creates intensity with
            # new blue and red
            set_color(new_image, x, y, sepia)  # sets pixel to new intensity

        elif r >= 63 and r <= 191:  # checks if the red value is between 63 and 191

            new_red = r * 1.15  # sets red to 115% of original intensity
            new_blue = b * 0.85  # sets blue to 85% of original intensity
            
            sepia = create_color(new_red, g, new_blue)
            set_color(new_image, x, y, sepia)

        else:
            
            new_red = r * 1.08  # sets red to 108% of original intensity
            new_blue = b * 0.93  # sets blue to 93% of original intensity
            
            sepia = create_color(new_red, g, new_blue)
            set_color(new_image, x, y, sepia)

    return new_image


# Posterizing image filter
def adjust_component(r, g, b):  # this is the helping function

    """
    Created by Ben Li
    on March 16th, 2020
    
    Returning three values (red, green and blue) by calling the inside function (get_new_value) with 3 values r,g,b
    
    """

    def get_new_value(old_value):
        
        """
        Created by Ben Li
        on March 16th, 2020

        Returns new value of rgb based on old rgb value

        >>>get_new_value(23)
        31
        >>>get_new_value(65)
        95
        >>>get_new_value(192)
        223
        
        """
        
        if 0 <= old_value <= 63:
            
            return 31
        
        elif 64 <= old_value <= 127:
            
            return 95
        
        elif 128 <= old_value <= 191:
            
            return 159
        
        elif 192 <= old_value <= 255:
            
            return 223

        # if value between 0-63: return 31 , between 64-127: return 95 between 128-191: return 159, between 192-255:
        # return 223 (rgb values)

    r = get_new_value(r)
    b = get_new_value(b)
    g = get_new_value(g)

    return (r, g, b)


def posterizing(image: Image) -> Image:  # This is the main function for posterizing

    """
    Created by Ben Li
    on March 16th, 2020
    to apply a posterizing filter to an image
    
    Returns a copy of the original image with a posterizing filter applied to it

    >>> image = load_image(choose_file())
    >>> new_image = posterizing(image)
    >>> show(new_image)
    
    """
    new_image = copy(image)

    '''
    to make the image with smaller rgb amount(blurry) and keep the image look the same
    after select an image this will copy an image and look for every pixel in image.
    calling the _adjust_component function and create new color.
    at last set the new color for every pixel and return a new image.
    '''
    for pixel in new_image:
        
        x, y, (r, g, b) = pixel
        
        new_color = create_color(*adjust_component(r, g, b))
        set_color(new_image, x, y, new_color)

    return new_image


# edge detection image filter
def detect_edges(image: Image, threshold: int) -> Image:
    
    """
    Created by Abraham Paulose
    on March 20th, 2020
    to apply an edge detection filter to an image
    
    Return a new copy of the original image, which has a filter applied to it, making the image look like a pencil sketch

    >>> image = load_image(choose_file())
    >>> edges_image = detect_edges(image,8)
    >>> show(edges_image)
    
    """
    new_image = copy(image)

    for width in range(get_width(new_image) - 1):  # Goes through the width of image

        for height in range(get_height(new_image) - 1):  # Goes through the height of image

            pixel_1 = get_color(image, width, height)
            pixel_2 = get_color(image, width, height + 1)

            if abs(((pixel_1[0] + pixel_1[1] + pixel_1[2]) / 3) - (
                    (pixel_2[0] + pixel_2[1] + pixel_2[2]) / 3)) > threshold:

                new_image.set_color(width, height, create_color(0, 0, 0))
                # Creates the color black

            else:

                new_image.set_color(width, height, create_color(255, 255, 255))
                # Creates the color white

    for width in range(get_width(new_image)):
        
        new_image.set_color(width, new_image.get_height() - 1, create_color(255, 255, 255))

    return new_image


# Improved edge detection image filter
def detect_edges_better(image: Image, threshold: int) -> Image:
    
    """
    Created by Yash Kapoor 
    on March 21st, 2020
    to apply an improved version of the edge detection filter to an image
    
    Return a new copy of the original image, which has a filter applied to it, making the image look like a pencil sketch

    >>> image = load_image(choose_file())
    >>> edges_better_image = detect_edges_better(image,8)
    >>> show(edges_better_image)
    
    """
    
    new_image = copy(image)

    for width in range(get_width(new_image) - 1):
        # using a for loop to get the width dimensions of the image

        for height in range(get_height(new_image) - 1):
            # using a nested for loop to get the height dimensions of the image

            pixel_1 = get_color(image, width, height)
            # gets the color of all the pixels of the image chosen by the user

            pixel_2 = get_color(image, width, height + 1)
            # gets the color of all the pixels of the image chosen by the user and it is one below pixel_1

            pixel_3 = get_color(image, width + 1, height)
            # gets the color of all the pixels of the image chosen by the user and it is one to the right of pixel_1

            if abs(((pixel_1[0] + pixel_1[1] + pixel_1[2]) / 3) - (
                    (pixel_2[0] + pixel_2[1] + pixel_2[2]) / 3)) > threshold:
                # if the contrast between the pixel subtracted by the pixel below it is greater than the threshold, the
                # contrast between the two pixels is high

                new_image.set_color(width, height, create_color(0, 0, 0))
            # changing the top pixel's colour to black if the contrast between the two pixels is high

            elif abs(((pixel_1[0] + pixel_1[1] + pixel_1[2]) / 3) - (
                    (pixel_3[0] + pixel_3[1] + pixel_3[2]) / 3)) > threshold:
                # if the contrast between the pixel subtracted by the pixel to the right of it is greater than the threshold, the
                # contrast between the two pixels is high

                new_image.set_color(width, height, create_color(0, 0, 0))
            # changing the original pixel's colour to black if the contrast between the original pixel and the pixel to
            # the right is high

            else:

                new_image.set_color(width, height, create_color(255, 255, 255))

    for width in range(get_width(new_image)):
        # using a for loop to set the colour of the bottom row, which has no pixels below it, to white

        new_image.set_color(width, new_image.get_height() - 1, create_color(255, 255, 255))

    for height in range(get_height(new_image)):
        # using a for loop to set the colour of the last column, which has no pixels to the right of it, to white

        new_image.set_color(new_image.get_width() - 1, height, create_color(255, 255, 255))

    return new_image


# flip vertical image filter
def flip_vertical(image: Image) -> Image:
    
    """
    Created by Gordon Vanstokkom
    on March 22nd, 2020
    to flip an image vertically
    
    Returns a vertically flipped copy of a selected image.
    
    Example: if someone in the photo was looking to the left 
    they would now be looking to the right. 
   
    >>> image = load_image(choose_file())
    >>> flipped_image = flip_vertical(image)
    >>> show(flipped_image)
    
    """

    new_image = copy(image)  # make a copy and call it new_image
    
    for x, y, (r, g, b) in image:  # for every pixle in origional do this
        
        new_color = get_color(image, (-x - 1), y)  # get color from a reverse iteration
        set_color(new_image, x, y, new_color)  # set new_image pixle to new_color

    return new_image


# flip horizontally image filter
def flip_horizontal(image: Image) -> Image:
    
    """
    Created by Ben Li
    on March 22nd, 2020
    to flip an image horizontally
    
    Returns a horizontally flipped copy of a selected image.

    >>> image = load_image(choose_file())
    >>> flipped_image = flip_horizontal(image)
    >>> show(flipped_image)
    
    """
    new_image = copy(image)
    
    for x, y, (r, g, b) in image:
        
        nc = get_color(image, (x), (-y - 1))
        set_color(new_image, x, y, nc)

    # Flip the image based on horizontal axis.
    # This function takes a image copy the image and for each pixel in the image
    # Get color of the image for x value and the invert of y value.
    # For example the first pixel's get color will have the color for first x value and the last y value.
    # Set the new color with every pixel through x,y with the new color.
    # Return the new image with new color got before

    return new_image


# Main Script

if __name__ == "__main__":

    user_filter_choice = ""  # declaring a variable and storing an empty string value in it to use in the while loop

    # This while loop below is created by Yash Kapoor by combining everyone's main script together to make it more organized
    while user_filter_choice != "Q":
        # As long as the user does not input "Q", all the code below will keep executing

        print("\nChoose which filter you want to apply to the image(s)")
        
        user_filter_choice = input(
            "\nR)ed\tG)reen\tB)lue\tC)ombined\nTwo) Tone\tThree) Tone\tE)xtreme Contrast\tS)epia\t\tP)osterizing\nEdge) Detection\t\tImproved Edge) Detection\tHorizontal) Flip\tVertical) Flip\n\n(Type Q to Quit) : ")


        if user_filter_choice == "Q":

            print("\nThank you for trying out this program!")


        elif user_filter_choice == "R" or user_filter_choice == "r":

            file = choose_file()
            image = load_image(file)
            new = red_channel(image)
            show(new)


        elif user_filter_choice == "G" or user_filter_choice == "g":

            file = choose_file()
            image = load_image(file)
            function = pic_to_green(image)
            show(function)  # shows the image that has gone through the pic_to_green function


        elif user_filter_choice == "B" or user_filter_choice == "b":

            file = choose_file()
            image = load_image(file)
            # allows the user to choose an image from their computer

            filter_function = color_filter(
                image)  # Calling the filter function that takes the original image as an argument
            show(filter_function)  # Displaying the new image that is stored in the variable called filter_function


        elif user_filter_choice == "C" or user_filter_choice == "c":

            file = choose_file()
            image_a = load_image(file)

            file = choose_file()
            image_b = load_image(file)

            file = choose_file()
            image_c = load_image(file)
            # allowing the user to choose three images from their computer to test the combined filter

            image_combined = combine(image_a, image_b, image_c)

            '''
            Calling the combined function and passing on the three images that were chosen by the user as arguments, so the function can combine them
            '''

            show(image_combined)

        elif user_filter_choice == "Two" or user_filter_choice == "two":

            file = choose_file()
            image = load_image(file)
            
            #allowing the user to input two colors 
            first = input("Enter the first colour: ").lower()
            second = input("Enter the second colour: ").lower()

            image_two_tone = two_tone(image, first, second)

            show(image_two_tone)

        elif user_filter_choice == "Three" or user_filter_choice == "three":

            file = choose_file()
            image = load_image(file)
            
            #allowing the user to input three colors that are in the list called color
            first = input("Enter the first colour: ").lower()
            second = input("Enter the second colour: ").lower()
            third = input("Enter the third colour: ").lower()

            image_three_tone = three_tone(image, first, second, third)

            show(image_three_tone)

        elif user_filter_choice == "E" or user_filter_choice == "e":

            image = load_image(choose_file())

            show(extreme_contrast(image))

        elif user_filter_choice == "S" or user_filter_choice == "s":

            file = choose_file()
            image = load_image(file)
            new_image = sepia(image)
            show(new_image)

        elif user_filter_choice == "P" or user_filter_choice == "p":

            image = load_image(choose_file())

            show(posterizing(image))

        elif user_filter_choice == "Edge" or user_filter_choice == "edge":

            image = load_image(choose_file())

            show(detect_edges(image, 8))

        elif user_filter_choice == "Improved Edge" or user_filter_choice == "improved edge":

            image = load_image(choose_file())

            show(detect_edges_better(image, 8))

        elif user_filter_choice == "Horizontal" or user_filter_choice == "horizontal":

            image = load_image(choose_file())

            show(flip_horizontal(image))

        else:

            # This is to flip the image vertically
            file = choose_file()
            image = load_image(file)

            new = flip_vertical(image)
            show(new)
