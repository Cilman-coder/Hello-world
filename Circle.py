import math
import turtle

def drawCircle(t, centerX, centerY, radius):
    """
    Draws a circle using a Turtle object.

    Parameters:
        t (turtle.Turtle): The Turtle object used for drawing
        centerX (float): x-coordinate of the circle's center
        centerY (float): y-coordinate of the circle's center
        radius (float): radius of the circle
    """

    # Move turtle to the starting point (rightmost point of the circle)
    
    t.penup()
    t.goto(centerX + radius, centerY)
    t.setheading(90)  # Point upward
    t.pendown()

    # Calculate step size for 120 segments (each 3°)
    
    step_length = 2.0 * math.pi * radius / 120.0

    # Draw the circle
    
    for _ in range(120):
        t.left(3)
        t.forward(step_length)


# Example test (can be removed when imported)

if __name__ == "__main__":
    wn = turtle.Screen()
    wn.title("Draw Circle Example")

    t = turtle.Turtle()
    t.speed(0)

    drawCircle(t, 0, 0, 100)

    
