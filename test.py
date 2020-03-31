import PIL.Image

image = PIL.Image.open("b.png")
width, height = image.size

print(width, height)