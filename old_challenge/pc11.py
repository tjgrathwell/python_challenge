from PIL import Image

im = Image.open("cave.jpg")
even = Image.new(im.mode, (320,240))
odd = Image.new(im.mode, (320,240))

for i in range(0,im.size[0]):
    for j in range(0, im.size[1]):
        if ((i%2) == 0):
            if ((j%2) == 0):
                even.putpixel((i/2, j/2), im.getpixel((i,j)))
        elif ((j%2) != 0):
            odd.putpixel(((i-1)/2, (j-1)/2), im.getpixel((i,j)))

even.save("even.jpg", "JPEG")
odd.save("odd.jpg", "JPEG")