import turtle
import math

def drawFractalLine(distance, direction, level):
   """
   Draw one Koch fractal side.
   `direction` is an absolute heading in degrees (0 east).
   """
   if level == 0:
       turtle.setheading(direction)
       turtle.forward(distance)
   else:
       third = distance / 3.0
       
       # Subdivide into four fractal pieces with appropriate headings
       
       drawFractalLine(third, direction, level - 1)
       drawFractalLine(third, direction + 60, level - 1)
       drawFractalLine(third, direction - 60, level - 1)
       drawFractalLine(third, direction, level - 1)

def main():
    
   # Requested parameters
   
   width = 200
   height = 200
   size = 150
   level = 4

   screen = turtle.Screen()
   screen.setup(width, height)
   screen.title(f"Koch Snowflake — Level {level}")

   turtle.hideturtle()
   turtle.speed(0)
   turtle.pensize(1)
   turtle.penup()

   # Centering: start at lower-left vertex of an equilateral triangle of side size
   
   tri_height = math.sqrt(3) / 2 * size
   start_x = -size / 2
   start_y = -tri_height / 3  
   turtle.goto(start_x, start_y)
   turtle.pendown()

   # Draw the three Koch sides (absolute headings 0, -120, 120)
   
   drawFractalLine(size, 0, level)
   drawFractalLine(size, -120, level)
   drawFractalLine(size, 120, level)

   turtle.penup()
   turtle.hideturtle()
   turtle.done()

if __name__ == "__main__":
   main()
