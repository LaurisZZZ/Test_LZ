import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Move the Turtle!")
screen.bgcolor("white")

# Create the turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.speed(10)

# Define movement functions
def move_forward():
    player.forward(50)

def move_backward():
    player.backward(50)

def turn_left():
    player.left(45)

def turn_right():
    player.right(45)

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Keep the window open
screen.mainloop()