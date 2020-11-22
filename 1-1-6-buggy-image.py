class a116_buggy_image_pm_version_5_12:
    def __init__(self):
        x = trtl.Turtle()
        x.pensize(40)
        x.circle(20)
        legs = 6
        rotate = 70
        degree = 380 / legs
        x.pensize(5)
        loop = 0
        while loop < legs:
            x.goto(0, 0)
            x.setheading(degree * loop)
            x.forward(rotate)
            loop = loop + 1
        x.hideturtle()
        wn = trtl.Screen()
        wn.mainloop()


class a116_buggy_image_pm_version_22_24:
    def __init__(self):
        #  Create a spider body ---
        x = trtl.Turtle()
        x.pensize(40)
        x.circle(20)
        # Configure Spider Legs----
        legs = 6
        rotate = 70
        degree = 380 / legs
        x.pensize(5)
        # ------------------------
        loop = 0
        while loop < legs:
            x.goto(0, 0)
            x.setheading(degree * loop)
            x.forward(rotate)
            loop = loop + 1
        # Draw spider legs -------
        x.hideturtle()
        wn = trtl.Screen()
        wn.mainloop()


class a116_buggy_image_pm_version_25_28:
    def __init__(self):
        #  Create a spider body ---
        x = trtl.Turtle()
        x.pensize(40)
        x.circle(20)
        # Configure Spider Legs----
        legs = 8
        rotate = 70
        degree = 360 / legs
        x.pensize(5)
        # ------------------------
        loop = 0
        while loop < legs:
            x.goto(0, 20)
            x.setheading(degree * loop)
            x.forward(rotate)
            loop = loop + 1
        # Draw spider legs -------
        x.hideturtle()
        wn = trtl.Screen()
        wn.mainloop()


class a116_buggy_image_pm_version_29_31:
    #i dont know how to do the other
    def __init__(self):
        #  Create a spider body ---
        x = trtl.Turtle()
        x.pensize(40)
        x.circle(20)
        # Configure Spider Legs----
        legs = 8
        rotate = 70
        angle = 360 / legs
        x.pensize(5)
        # ------------------------
        loop = 0
        while loop < legs:
            x.goto(0, 20)
            x.setheading((angle * loop) - 45)
            x.forward(rotate)
            loop = loop + 1
        # Draw spider legs -------
        x.hideturtle()
        wn = trtl.Screen()
        wn.mainloop()


if __name__ == '__main__':
    a116_buggy_image_pm_version_29_31()
