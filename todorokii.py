
import pywhatkit as pw
from PIL import Image

source = "as.jpg"
destination = "as.txt"

image_path = "as.jpg"
img = Image.open(image_path)


pw.image_to_ascii_art(source, destination)

width, height = img.size
aspect_ratio = height/width
new_width = 200
new_height = aspect_ratio*new_width*0.48
img = img.resize((new_width, int(new_height)))

img = img.convert('L')

pixels = img.getdata()

# pixeli eşit uzunluktaki karakterle değiştiriyom
chars = ["B", "S", "#", "&", "@", "$", "%",
         "*", "!", ":", ".", "/", "(", "[", ",", "7"]
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width]
               for index in range(0, new_pixels_count, new_width)]
ascii_image = "/n".join(ascii_image)

txt_path = "ass.txt"

with open("as.txt", "w") as f:
    f.write(ascii_image)
