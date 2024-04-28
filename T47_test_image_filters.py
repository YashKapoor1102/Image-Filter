""" 
ECOR 1051 Winter 2020
Project Milestone 2

Created by Team 47
Members: Yash Kapoor: 101163338 (Team Leader), Gordon Vanstokkom: 100980313, Abraham Paulose: 101168299 and Ben Li: 101113284
on March 25th, 2020
to test different filters to ensure they pass every test

"""

from Cimpl import *
from unit_testing import check_equal
from T47_image_filters import *


#Test for blue filter
def test_bluechannel() -> None:
    
    """
    Created by Yash Kapoor
    on March 8th, 2020
    
    A test function that checks to see if every pixel turns into blue 
    
    >>> test_bluechannel()
    
    Checking pixel @(0, 0) PASSED
    
    Checking pixel @(1, 0) PASSED
    
    Checking pixel @(2, 0) PASSED
    
    Checking pixel @(3, 0) PASSED

    """

    # This test function ensures that the following pixels from the original image have correctly transformed into blue:
    # (135, 106, 76) to (0, 0, 76)
    # (137, 110, 80) to (0, 0, 80)
    # (151, 126, 95) to (0, 0, 95)
    # (130, 107, 73) to (0, 0, 73)
    # (141, 122, 79) to (0, 0, 79)
    # (134, 114, 64) to (0, 0, 64)
    # (141, 122, 64) to (0, 0, 64)
    # (144, 122, 62) to (0, 0, 62)

    # If these pixels have correctly transformed into blue, the message, "PASSED", will be displayed to the user
    # If they have not transformed into blue, the message, "FAILED", will be displayed to the user

    original = create_image(8, 1)
    # Create an image with eight pixels

    set_color(original, 0, 0, create_color(135, 106, 76))
    set_color(original, 1, 0, create_color(137, 110, 80))
    set_color(original, 2, 0, create_color(151, 126, 95))
    set_color(original, 3, 0, create_color(130, 107, 73))
    set_color(original, 4, 0, create_color(141, 122, 79))
    set_color(original, 5, 0, create_color(134, 114, 64))
    set_color(original, 6, 0, create_color(141, 122, 64))
    set_color(original, 7, 0, create_color(144, 122, 62))

    expected = create_image(8, 1)
    # Create an image that is identical to the original one with the same number of pixels but different color

    set_color(expected, 0, 0, create_color(0, 0, 76))
    set_color(expected, 1, 0, create_color(0, 0, 80))
    set_color(expected, 2, 0, create_color(0, 0, 95))
    set_color(expected, 3, 0, create_color(0, 0, 73))
    set_color(expected, 4, 0, create_color(0, 0, 79))
    set_color(expected, 5, 0, create_color(0, 0, 64))
    set_color(expected, 6, 0, create_color(0, 0, 64))
    set_color(expected, 7, 0, create_color(0, 0, 62))

    blue_image = color_filter(original)

    for x, y, col in blue_image:  # col is the Color object for the pixel @ (x,y)
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


#Test for green filter
def test_greenchannel() -> None:

    """
    Created by Abraham Paulose
    on March 8th, 2020
    
    A testing function for the pic_to_green function where it creates an image with eight pixels, runs it through
    the pic_to_green function and compares it with the original image(eight pixels) but turned green.

    >>> test_greenchannel()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED


    """

    original = create_image(8, 1)  # Create an image with eight pixels.

    set_color(original, 0, 0, create_color(135, 106, 76))
    set_color(original, 1, 0, create_color(137, 110, 80))
    set_color(original, 2, 0, create_color(151, 126, 95))
    set_color(original, 3, 0, create_color(130, 107, 73))
    set_color(original, 4, 0, create_color(141, 122, 79))
    set_color(original, 5, 0, create_color(134, 114, 64))
    set_color(original, 6, 0, create_color(141, 122, 64))
    set_color(original, 7, 0, create_color(144, 122, 62))

    expected = create_image(8, 1)
    # Create an image that is identical to the original one with the same number of pixels but each pixel retains only the
    # green colour

    set_color(expected, 0, 0, create_color(0, 106, 0))
    set_color(expected, 1, 0, create_color(0, 110, 0))
    set_color(expected, 2, 0, create_color(0, 126, 0))
    set_color(expected, 3, 0, create_color(0, 107, 0))
    set_color(expected, 4, 0, create_color(0, 122, 0))
    set_color(expected, 5, 0, create_color(0, 114, 0))
    set_color(expected, 6, 0, create_color(0, 122, 0))
    set_color(expected, 7, 0, create_color(0, 122, 0))

    green_image = pic_to_green(original)

    for x, y, col in green_image:  # col is the Colour object for the pixel @ (x,y)

        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


#Test for red filter
def test_redchannel() -> None: 
    
    """
    Created by Gordon Vanstokkom
    on March 8th, 2020
    
    A test function for the red filter
    
    >>> test_redchannel()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED

    
    """
    # This test function checks if grayscale correctly transforms:
    # (0, 0, 0) to (0, 0, 0)  # the darkest gray shade
    # (0, 0, 1) to (0, 0, 0)  # the darkest non-gray shade
    # (127, 127, 127) to (127, 127, 127)  # a mid-range gray shade
    # (125, 73, 224) to (140, 140, 140)   # a non-gray colour
    # (254, 255, 255) to (254, 254, 254)  # the brightest non-gray shade  
    # (255, 255, 255) to (255, 255, 255)  # the brightest gray shade

    # Create an image with six pixels.

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(127, 0, 0))
    set_color(expected, 3, 0, create_color(140, 0, 0))
    set_color(expected, 4, 0, create_color(254, 0, 0))
    set_color(expected, 5, 0, create_color(255, 0, 0))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    red_image = red_channel(original)
    
    for x, y, col in red_image:  # col is the Color object for the pixel @ (x,y)
        
        # There's no need to unpack that object into
        # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


#Test for combine filter
def test_combine() -> None:  

    """
    Created by Ben Li
    on March 8th, 2020
    
    A test function that checks to see if the three images that are chosen by the user, have successfully combined their RGB values to form a new copy of the image 
    
    >>> test_combine()
    
    Checking pixel @(0, 0) PASSED
    
    Checking pixel @(1, 0) PASSED
    
    Checking pixel @(2, 0) PASSED
    
    Checking pixel @(3, 0) PASSED
    
    
    """

    image_red = create_image(8, 1)
    # Creates an image that contains the values for the color red

    set_color(image_red, 0, 0, create_color(135, 0, 0))
    set_color(image_red, 1, 0, create_color(137, 0, 0))
    set_color(image_red, 2, 0, create_color(151, 0, 0))
    set_color(image_red, 3, 0, create_color(130, 0, 0))
    set_color(image_red, 4, 0, create_color(141, 0, 0))
    set_color(image_red, 5, 0, create_color(134, 0, 0))
    set_color(image_red, 6, 0, create_color(141, 0, 0))
    set_color(image_red, 7, 0, create_color(144, 0, 0))

    image_green = create_image(8, 1)
    # Creates an image that contains the values for the color green

    set_color(image_green, 0, 0, create_color(0, 106, 0))
    set_color(image_green, 1, 0, create_color(0, 110, 0))
    set_color(image_green, 2, 0, create_color(0, 126, 0))
    set_color(image_green, 3, 0, create_color(0, 107, 0))
    set_color(image_green, 4, 0, create_color(0, 122, 0))
    set_color(image_green, 5, 0, create_color(0, 114, 0))
    set_color(image_green, 6, 0, create_color(0, 122, 0))
    set_color(image_green, 7, 0, create_color(0, 122, 0))

    image_blue = create_image(8, 1)
    # Creates an image that contains the values for the color blue

    set_color(image_blue, 0, 0, create_color(0, 0, 76))
    set_color(image_blue, 1, 0, create_color(0, 0, 80))
    set_color(image_blue, 2, 0, create_color(0, 0, 95))
    set_color(image_blue, 3, 0, create_color(0, 0, 73))
    set_color(image_blue, 4, 0, create_color(0, 0, 79))
    set_color(image_blue, 5, 0, create_color(0, 0, 64))
    set_color(image_blue, 6, 0, create_color(0, 0, 64))
    set_color(image_blue, 7, 0, create_color(0, 0, 62))

    expected = create_image(8, 1)
    # Create a single new image that is produced by combining the pixels for Red, Green and Blue images/values

    set_color(expected, 0, 0, create_color(135, 106, 76))
    set_color(expected, 1, 0, create_color(137, 110, 80))
    set_color(expected, 2, 0, create_color(151, 126, 95))
    set_color(expected, 3, 0, create_color(130, 107, 73))
    set_color(expected, 4, 0, create_color(141, 122, 79))
    set_color(expected, 5, 0, create_color(134, 114, 64))
    set_color(expected, 6, 0, create_color(141, 122, 64))
    set_color(expected, 7, 0, create_color(144, 122, 62))

    combined_image = combine(image_red, image_green, image_blue)
    # Storing the combined image that the combined function returns in the variable called combined_image

    for x, y, col in combined_image:  # col is the Color object for the pixel @ (x,y)
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


#Test for two tone filter
def test_two_tone() -> None:
    
    """
    Created by Yash Kapoor
    on March 14th, 2020
    
    A test function for the two tone filter function that creates an image with eight pixels, runs it through the
    two_tone filter function and compares it with the original image to ensure the filter function is working properly

    >>> test_two_tone()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED

    
    """

    '''
    If the pixel's brightness is between 0 and 127, the colour will be turned to the first colour entered by the user. 
    On the other hand, if the pixel's brightness is between 128 and 255, the colour will be turned to the second colour entered.
    
    '''

    print("\nTesting two_tone function\n")

    # User inputs first and second color of their choice (must be chosen from the set called Colors)

    first = input("Enter the first colour: ").lower()
    second = input("Enter the second colour: ").lower()

    print("\n")

    original = create_image(8, 1)  # Create an image with eight pixels.

    set_color(original, 0, 0, create_color(135, 136, 176))
    set_color(original, 1, 0, create_color(137, 110, 180))
    set_color(original, 2, 0, create_color(151, 126, 135))
    set_color(original, 3, 0, create_color(130, 107, 173))
    set_color(original, 4, 0, create_color(14, 12, 79))
    set_color(original, 5, 0, create_color(34, 95, 64))
    set_color(original, 6, 0, create_color(127, 110, 120))
    set_color(original, 7, 0, create_color(100, 90, 63))

    expected = create_image(8, 1)
    # Create an image that is identical to the original one with the same number of pixels but each pixel
    # has values that retain a certain color depending on what the average of the RGB components is

    set_color(expected, 0, 0, create_color(*Colors[second]))
    set_color(expected, 1, 0, create_color(*Colors[second]))
    set_color(expected, 2, 0, create_color(*Colors[second]))
    set_color(expected, 3, 0, create_color(*Colors[second]))
    set_color(expected, 4, 0, create_color(*Colors[first]))
    set_color(expected, 5, 0, create_color(*Colors[first]))
    set_color(expected, 6, 0, create_color(*Colors[first]))
    set_color(expected, 7, 0, create_color(*Colors[first]))

    two_tone_image = two_tone(original, first, second)
    # passing on the original image and the colors that the user enters as arguments to ensure the test function works properly

    for x, y, col in two_tone_image:  # col is the Colour object for the pixel @ (x,y)

        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



#Test for three tone filter
def test_three_tone() -> None:
    
    """
    Created by Yash Kapoor
    on March 15th, 2020
    
    A test function for the three tone filter function that creates an image with eight pixels, runs it through the
    three_tone filter function and compares it with the original image to ensure the filter function is working properly

    >>> test_three_tone()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED

    
    """
    print("\nTesting three_tone function\n")

    '''
    If the pixel's brightness is between 0 and 84, the colour will be turned to the first colour entered by the user.
    Otherwise, if the pixel's brightness is between 85 and 170, the colour will be turned to the second colour.
    Otherwise, if the pixel's brightness is between 171 and 255, the colour will be turned to the third colour.
    
    '''

    # User inputs first, second and third color of their choice (must be chosen from the set called Colors)

    first = input("Enter the first colour: ").lower()
    second = input("Enter the second colour: ").lower()
    third = input("Enter the third colour: ").lower()

    print("\n")

    original = create_image(8, 1)  # Create an image with eight pixels.

    set_color(original, 0, 0, create_color(135, 136, 176))
    set_color(original, 1, 0, create_color(185, 200, 180))
    set_color(original, 2, 0, create_color(151, 126, 250))
    set_color(original, 3, 0, create_color(130, 107, 173))
    set_color(original, 4, 0, create_color(14, 12, 79))
    set_color(original, 5, 0, create_color(34, 95, 64))
    set_color(original, 6, 0, create_color(127, 110, 120))
    set_color(original, 7, 0, create_color(100, 90, 50))

    expected = create_image(8, 1)
    # Create an image that is identical to the original one with the same number of pixels but each pixel 
    # has values that retain a certain color depending on what the average of the RGB components is

    set_color(expected, 0, 0, create_color(*Colors[second]))
    set_color(expected, 1, 0, create_color(*Colors[third]))
    set_color(expected, 2, 0, create_color(*Colors[third]))
    set_color(expected, 3, 0, create_color(*Colors[second]))
    set_color(expected, 4, 0, create_color(*Colors[first]))
    set_color(expected, 5, 0, create_color(*Colors[first]))
    set_color(expected, 6, 0, create_color(*Colors[second]))
    set_color(expected, 7, 0, create_color(*Colors[first]))

    three_tone_image = three_tone(original, first, second, third)
    # passing on the original image and the colors that the user enters as arguments to ensure the test function works properly

    for x, y, col in three_tone_image:  # col is the Colour object for the pixel @ (x,y)

        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


#Test for extreme contrast filter
def test_extreme() -> None:
    
    """
    Created by Abraham Paulose
    on March 16th, 2020
    
    A test function for extreme_contrast

    >>> testing_function()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED

    """
    
    original = create_image(8, 1)  # Create an image with eight pixels.
    set_color(original, 0, 0, create_color(135, 136, 176))
    set_color(original, 1, 0, create_color(137, 110, 180))
    set_color(original, 2, 0, create_color(151, 126, 135))
    set_color(original, 3, 0, create_color(130, 107, 173))
    set_color(original, 4, 0, create_color(14, 12, 79))
    set_color(original, 5, 0, create_color(34, 95, 64))
    set_color(original, 6, 0, create_color(127, 110, 120))
    set_color(original, 7, 0, create_color(100, 90, 63))

    expected = create_image(8, 1)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(255, 0, 255))
    set_color(expected, 2, 0, create_color(255, 0, 255))
    set_color(expected, 3, 0, create_color(255, 0, 255))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(0, 0, 0))
    set_color(expected, 6, 0, create_color(0, 0, 0))
    set_color(expected, 7, 0, create_color(0, 0, 0))

    contrast_image = extreme_contrast(original)  # Extreme_contrast function is done by Yash Kapoor.

    for x, y, col in contrast_image:  # Col is the Colour object for the pixel @ (x,y)

        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



#Test for sepia filter
def test_sepia() -> None:
    """
    Created by Ben Li
    on March 16th, 2020
    
    A test function for Sepia that creates an image with six pixels, runs it through the sepia filter function, and compares it with the original image to ensure the filter function is working properly

    >>> test_sepia()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED

    """

    original = create_image(6, 1)
    # Create an image with 6 pixels.
    # from test_grayscale in culearn milestone1 P1 Task 4 - A folder containing Cimpl.py and Approved Sample Images
    # expected value from example goes to original color

    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))
    expected = create_image(6, 1)

    # from sepia function sub the values into if statement and *1.15 or *0.85 and put it here
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(146, 127, 107))
    set_color(expected, 3, 0, create_color(161, 140, 119))
    set_color(expected, 4, 0, create_color(274, 254, 236))
    set_color(expected, 5, 0, create_color(275, 255, 237))

    sepia_image = sepia(original)

    for x, y, col in sepia_image:  # col is the Colour object for the pixel @ (x,y)

        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



#Test for posterizing filter
def test_posterizing() -> None:
    """     
    Created by Gordon Vanstokkom
    on March 16th, 2020
    
    A test function for posterizing.
    Tests whether or not the posterizing function
    worked the way it should.
    
    >>> test_posterizing()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED

    """

    # Create an image with six pixels.

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    # Create an image that's identical to the one a correct implementation of
    # posterizing should produce when it is passed original.

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(31, 31, 31))
    set_color(expected, 1, 0, create_color(31, 31, 31))
    set_color(expected, 2, 0, create_color(95, 95, 95))
    set_color(expected, 3, 0, create_color(95, 95, 223))
    set_color(expected, 4, 0, create_color(223, 223, 223))
    set_color(expected, 5, 0, create_color(223, 223, 223))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    posterized_image = posterizing(original)

    for x, y, col in posterized_image:
        
        # col is the Color object for the pixel @ (x,y)
        # There's no need to unpack that object into
        # RGB components.
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



#Test for edge detection filter 
def test_detect_edges() -> None:
    
    """
    Created by Yash Kapoor
    on March 22nd, 2020
    
    A test function for the Edge Detection Filter that creates an image with eight pixels, runs it through the
    detect_edges filter function and compares it with the original image to ensure the filter function is working properly

    >>> test_detect_edges()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(0, 1) PASSED

    Checking pixel @(0, 2) PASSED

    Checking pixel @(0, 3) PASSED

    """

    original = create_image(8, 8)  # Create an image with eight pixels in x and y.

    set_color(original, 0, 0, create_color(135, 136, 176))
    set_color(original, 0, 1, create_color(185, 200, 180))
    set_color(original, 0, 2, create_color(205, 126, 250))
    set_color(original, 0, 3, create_color(130, 107, 173))
    set_color(original, 0, 4, create_color(250, 100, 79))
    set_color(original, 0, 5, create_color(34, 95, 64))
    set_color(original, 0, 6, create_color(127, 110, 120))
    set_color(original, 0, 7, create_color(100, 90, 50))

    expected = create_image(8, 8)
    # Create an image that is identical to the original one with the same number of pixels but each pixel 
    # has values that retain a certain color depending on whether the color changes to black or white

    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 0, 2, create_color(0, 0, 0))
    set_color(expected, 0, 3, create_color(255, 255, 255))
    set_color(expected, 0, 4, create_color(0, 0, 0))
    set_color(expected, 0, 5, create_color(0, 0, 0))
    set_color(expected, 0, 6, create_color(0, 0, 0))
    set_color(expected, 0, 7, create_color(255, 255, 255))

    detect_edges_test = detect_edges(original, 8)
    # passing on the original image that has eight pixels in x and y to ensure the test function works properly

    for x, y, col in detect_edges_test:  # col is the Colour object for the pixel @ (x,y)

        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



#Test for improved edge detection filter
def testing_detect_edges_better() -> None:
    '''
    Created by Abraham Paulose
    on March 22nd, 2020
    
    A test function for the improved edge detection filter

    >>> testing_detect_edges_better()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    '''
    original = create_image(3, 3)  # Create an image with eight pixels.
    set_color(original, 0, 0, create_color(135, 136, 176))
    set_color(original, 1, 0, create_color(137, 110, 180))
    set_color(original, 2, 0, create_color(151, 126, 135))
    set_color(original, 0, 1, create_color(14, 12, 79))
    set_color(original, 1, 1, create_color(34, 95, 64))
    set_color(original, 2, 1, create_color(127, 110, 120))
    set_color(original, 0, 2, create_color(130, 107, 173))
    set_color(original, 1, 2, create_color(14, 12, 79))
    set_color(original, 2, 2, create_color(34, 95, 64))

    expected = create_image(3, 3)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(0, 0, 0))
    set_color(expected, 2, 1, create_color(255, 255, 255))
    set_color(expected, 0, 2, create_color(255, 255, 255))
    set_color(expected, 1, 2, create_color(255, 255, 255))
    set_color(expected, 2, 2, create_color(255, 255, 255))

    edge_image = detect_edges_better(original, 8)  # Detect_edges_better function is done by Yash Kapoor.
    
    for x, y, col in edge_image:  # col is the Colour object for the pixel @ (x,y)
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



#Test for flip horizontal filter
def test_flip_horizontal() -> None:
    
    """
    Created by Gordon Vanstokkom 
    on March 23rd, 2020
    
    A test function for flip_horizontal.
    
    Tests whether or not the flip_horizontal function
    worked the way it should.
    
    >>> test_flip_horizontal()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(0, 1) PASSED

    Checking pixel @(0, 2) PASSED

    Checking pixel @(0, 3) PASSED

    """

    # Create an image with six pixels.

    original = create_image(1, 6)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(0, 0, 1))
    set_color(original, 0, 2, create_color(127, 127, 127))
    set_color(original, 0, 3, create_color(125, 73, 224))
    set_color(original, 0, 4, create_color(254, 255, 255))
    set_color(original, 0, 5, create_color(255, 255, 255))

    # Create an image that's identical to the one a correct implementation of
    # Test_flip_horizontal should produce when it is passed original.

    expected = create_image(1, 6)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(254, 255, 255))
    set_color(expected, 0, 2, create_color(125, 73, 224))
    set_color(expected, 0, 3, create_color(127, 127, 127))
    set_color(expected, 0, 4, create_color(0, 0, 1))
    set_color(expected, 0, 5, create_color(0, 0, 0))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    horizontally_flipped_image = flip_horizontal(original)
    
    for x, y, col in horizontally_flipped_image:
        
        # col is the Color object for the pixel @ (x,y)
        # There's no need to unpack that object into
        # RGB components.
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



#Test for flip vertical filter
def test_flip_vertical() -> None:
    """
    Created by Ben Li
    on March 23rd, 2020
    
    Compare the pixels with r,g,b color using check_equal function.
    Test function values original from flip_vertical expected values from sepia function.
    Out put pass or fail for each pixel check.

    >>> test_flip_vertical()

    Checking pixel @(0, 0) PASSED

    Checking pixel @(1, 0) PASSED

    Checking pixel @(2, 0) PASSED

    Checking pixel @(3, 0) PASSED

    """

    # Create an image with six pixels.
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    # Create image with opposite values of color on vertical axis.
    # Color on (0,0) from original color become the color on expected color (5,0)
    # so rbg on (1,0) match with (4,0) and so on.
    # Test_flip_vertical will result pass.

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(254, 255, 255))
    set_color(expected, 2, 0, create_color(125, 73, 224))
    set_color(expected, 3, 0, create_color(127, 127, 127))
    set_color(expected, 4, 0, create_color(0, 0, 1))
    set_color(expected, 5, 0, create_color(0, 0, 0))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    horizontally_flipped_image = flip_vertical(original)
    
    for x, y, col in horizontally_flipped_image:
        
        # col is the Color object for the pixel @ (x,y)
        # There's no need to unpack that object into
        # RGB components.
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# Main Script
if __name__ == "__main__":

    print("\nTest Function Created for Blue Filter\n")
    test_blue = test_bluechannel()

    print("\nTest Function Created for Green Filter\n")
    test_green = test_greenchannel()

    print("\nTest Function Created for Red Filter\n")
    test_red = test_redchannel()

    print("\nTest Function Created for Combine Filter\n")
    test_combine = test_combine()

    print("\nTest Function Created for Two Tone filter\n")
    test_two_tone = test_two_tone()

    print("\nTest Function Created for Three Tone filter\n")
    test_three_tone = test_three_tone()

    print("\nTest Function Created for Extreme Contrast Filter\n")
    test_extreme_contrast = test_extreme()

    print("\nTest Function Created for Sepia Filter\n")
    test_sepia = test_sepia()

    print("\nTest Function Created for Posterizing Filter\n")
    test_posterizing = test_posterizing()

    print("\nTest Function Created for Edge Detection Filter\n")
    test_detect_edges = test_detect_edges()

    print("\nTest Function Created for Improved Edge Detection Filter\n")
    test_improved_detect_edges = testing_detect_edges_better()

    print("\nTest Function Created for Flip Horizontal Filter\n")
    test_flip_horizontal = test_flip_horizontal()

    print("\nTest Function Created for Flip Vertical Filter\n")
    test_flip_vertical = test_flip_vertical()
