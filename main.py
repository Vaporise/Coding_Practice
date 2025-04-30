import turtle

screen = turtle.Screen() #creates a screen using the turtle library
screen.setup(1.0, 1.0) #setups up the screen to size 1 and position 1

t = turtle.Turtle() 

for c in ["red", "green", "blue", "yellow"]: #iterates through 4 colours where c is red/green/blue/yellow
    t.color(c) # set color to c
    t.forward(75) # move forward 75
    t.left(90) # turn left 90 degrees

screen.mainloop() #took out of for loop to fix issue.