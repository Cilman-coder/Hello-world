
from PIL import Image

def make_sepia(image_path, save_path):
   image = Image.open(smokey.gif)
   pixels = image.load()

   for y in range(image.height):
       for x in range(image.width):
           red, green, blue = image.getpixel((x, y))

           if red < 63:
               red = int(red * 1.1)
               blue = int(blue * 0.9)
           elif red < 192:
               red = int(red * 1.15)
               blue = int(blue * 0.85)
           else:
               red = min(int(red * 1.08), 255)
               blue = int(blue * 0.93)

           pixels[x, y] = (red, green, blue)

   image.save(smokey.gif)
   print("Sepia image saved to {smokey.gif}")

