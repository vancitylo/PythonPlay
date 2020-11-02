length = float(input("What is the length of your space?"))
width = float(input("What is the width of your space?"))
height = float(input("What is the height of your space?"))

area = length*width
vol = length*width*height

info = "The area of your space is {0:.2f}m2 and the volume of your space is {1:.2f}m3"
print(info.format(area,vol))