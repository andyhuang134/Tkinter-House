#note: some complicated colors do not work eg. light brown
from tkinter import *
import matplotlib

###------------Canvas Part Functions---------------###
def body(canvas,colour):
    canvas.create_rectangle(250,500,750,200,fill=colour)
    
def roof(canvas, colour):
    canvas.create_polygon(250,200,500,100,750,200,fill=colour) 
    
def door(canvas, colour):
    canvas.create_rectangle(600,350,500,500,fill=colour)
    
def portal(canvas,colour):
    canvas.create_oval(600,350,500,500,fill=colour)

def fence(canvas,colour):
    spacing1 = 0
    spacing2 = 0
    # adds one piece of fence every 40 pixels apart
    for fence in range(10):
        canvas.create_rectangle(1+spacing1,550,25+spacing1,900,fill=colour)
        spacing1 += 40
    for fence in range(7):   
        canvas.create_rectangle(965-spacing2,550,990-spacing2,900,fill=colour)
        spacing2 += 40
    # need a forloop to space out fence
    
def lawn(canvas,colour):
    canvas.create_rectangle(1,900,999,501,fill=colour)
    
def path(canvas,colour):
    canvas.create_polygon(500,500,400,900,500,900,fill=colour)
    canvas.create_polygon(600,500,700,900,600,900,fill=colour)
    canvas.create_rectangle(500,500,600,900,fill=colour,outline=colour)

def sun(canvas,colour):
    canvas.create_oval(75,50,200,170,fill=colour)
    
def sky(canvas,colour):
    canvas.create_rectangle(1,1,999,600,fill=colour)

def window(canvas,colour):
    canvas.create_rectangle(300,250,400,350,fill=colour,outline="black")
    canvas.create_line(350,250,350,350,fill="black")
    canvas.create_line(300,300,400,300,fill="black")
    
    
# colour list    
def colour_checker(): #fix choose colours
    # splits the color name by itself and appends into the list
    color_list = [color.split(':') for color in list(matplotlib.colors.get_named_colors_mapping().keys()) if len(color.split(":")) == 2]
    reversed_color_list = []
    
    # reverse the order of the split strings
    for color in color_list:
        color_pairs = color
        color_pairs.reverse()
        reversed_color_list.append(color_pairs)
    
    # appends the color name, and if there is 2 strings in list, it appends the first string which is the color name
    cleaned_color_list = [color[0] for color in reversed_color_list if len(color) != 1]
    return cleaned_color_list

# chooses colour
def choose_colour(canvas):
    colour_parts = ['sky','sun','body','window','roof','door','portal','lawn','fence','path']
    chosen_colour_list = []
    # user input colors for canvas parts
    for parts in colour_parts:
        chosen_colours = input(f"{parts} colour: ")
        chosen_colour_list.append(chosen_colours)
    
    # returns none if color is not in colour list
    for color in chosen_colour_list:
        if color not in colour_checker():
            print(f"invalid colour '{color}'")
            return None
        
    sky(canvas,chosen_colour_list[0])
    sun(canvas,chosen_colour_list[1])
    body(canvas,chosen_colour_list[2])
    window(canvas,chosen_colour_list[3])
    roof(canvas,chosen_colour_list[4])
    door(canvas,chosen_colour_list[5])
    portal(canvas,chosen_colour_list[6])
    lawn(canvas,chosen_colour_list[7])
    fence(canvas,chosen_colour_list[8])
    path(canvas,chosen_colour_list[9]) 
        
def main():
    root = Tk()
    root.geometry("1000x1000")
    canvas = Canvas(root, height=1000, width=1000)
    canvas.pack()
    colour_checker()
    choose_colour(canvas)
    
    
    root.mainloop()


if __name__ == "__main__":
    main()