#This program draws a circle each time you click on the screen.

import turtle
t, wn = turtle.Turtle(), turtle.Screen()

# turn animation of turtles off
t.hideturtle()
wn.tracer(0)

# set the width and height of our screen
width, height = 500, 500
wn.setup(width, height)

# 1. Create a function called get_quadrant_color:
#    a. it should have two parameters, click_x and click_y
#    b. the parameters represent the coordinates of where the mouse was when
#       when the screen was clicked
#    c. the function should return a string representing one of the following
#       four colors: red, green, blue and yellow
#    d. determine what color to give back based on what quadrant the user
#       clicked on:
#       * red - upper right
#       * green - lower right
#       * blue - upper left
#       * yellow - lower left
#  
# =====================================

def get_quadrant_color(click_x, click_y):
    if click_x > 0 and click_y > 0:
        return "red"
    elif click_x < 0 and click_y > 0:
        return "blue"
    elif click_x < 0 and click_y < 0:
        return "yellow"
    elif click_x > 0 and click_y < 0:
        return "green"

# (define get_quadrant_color here!)


def handle_click(x, y):
    # 2. pick your pen up
    # =====================================
    t.up()


    # 3. move your turtle to the x and y coordinates that are the parameters
    #    of this function
    # =====================================
    t.goto(x, y)


    # 4. put your pen back down
    # =====================================
    t.down()


    # 5. call your get_quadrant_color function here and save save the result 
    #    in a variable called quadrant_color
    # =====================================
    quadrant_color = get_quadrant_color(x, y)


    # 6. set the turtle's drawing color to the quadrant_color variable that 
    #    you created above
    # =====================================
    t.color(quadrant_color)


    # 7. draw a filled circle by calling the following methods on your
    #    *turtle object* in order:
    # 
    #    begin_fill()
    #    circle() <--- circle has radius as a parameter
    #    end_fill()
    # =====================================
    t.begin_fill()
    t.circle(69)
    t.end_fill()


# when the screen is clicked, call the handle_click function (and pass it the
# x and y coordinates
wn.onclick(handle_click)

wn.mainloop()
