from PIL import Image, ImageDraw
img = Image.new ('L', (960, 540), 255)
paint = ImageDraw.Draw(img)

with open('DS8.txt', 'r') as f:
    for line in f:
        list = line.split()
        i = int(list[1])
        j = int(list[0])
        paint.line((i, j, i+1, j+1))

img.show()
img.save('final.jpg')