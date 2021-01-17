'''
MECE E4606 - Assignment 1
@Author: James.F.VanHess@columbia.edu
@Description: Simple SVG generator example in Python
'''

#                                                                               #
# python script to generate a SVG file for cutting a rectagle with user input   #
#                                                                               #


# declaring global variables
# hardcoded svg strings
SVG_Header = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>"
SVG_Params = "<svg width=\"391\" height=\"391\" viewBox=\"-70.5 -70.5 391 391\" xmlns=\"http://www.w3.org/2000/svg\">"
SVG_Footer = "</svg>"
SVG_Rectangle = "<rect x=\"{}\" y=\"{}\" width=\"{}\" height=\"{}\" fill=\"green\" stroke-width=\"4\" stroke=\"pink\"/>".format(50, 40, 300, 150)


# get_Rectangle func Returns SVG string with rectangle
def get_Rectagle(x, y, width, height, stroke_width = 1, line_color = "black"):
    svg_rect = "<rect x=\"{}\" y=\"{}\" width=\"{}\" height=\"{}\" fill=\"none\" stroke-width=\"{}\" stroke=\"{}\"/>"
    
    return svg_rect.format(x, y, width, height, stroke_width, line_color)


def main():
    print(SVG_Header)

    # pars user input 
    rect_width = input("Please enter the width for your rectangle: \n")
    rect_height = input("Please enter the height for your rectangle: \n")

    rect_svg = get_Rectagle(20, 20, int(rect_width), int(rect_height), 1)
    with open('generated.svg', 'w') as svg_file:  
        # Write SVG Header
        svg_file.write(SVG_Header)  
        svg_file.write(SVG_Params)
       
        # Generate rectangles in a loop
        # change rectangle postion to (3*i, 3*i)
        for i in range(10):
            svg_file.write(get_Rectagle(3*i, 3*i, int(rect_width), 150, 1)
        # Write SVG Footer    
        svg_file.write(SVG_Footer)

    print('Created generated.svg')

# standard python way of calling the main function
# when the file is run as a script
if __name__ == "__main__":
    main()