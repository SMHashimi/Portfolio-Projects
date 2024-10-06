# extracting colors from an image
import colorgram
colors = colorgram.extract('image.jpg', 6)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_rgb_color = (r, g, b)
    rgb_colors.append(new_rgb_color)
image_5colors = [(220, 149, 107), (140, 119, 8), (73, 127, 125), (248, 254, 252), (14, 122, 175)] ##the first color was the background color
print(image_5colors)










