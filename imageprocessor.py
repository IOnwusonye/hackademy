from PIL import Image

def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image
    


im = Image.open("C:\\Users\\IOnwusonye\\Desktop\\pictures\\picture1.jpeg")
print(im.format, im.size, im.mode)

im = rotate_box(im)

im2 = Image.open("C:\\Users\\IOnwusonye\\Desktop\\pictures\\picture2.jpg")
im2 = rotate_box(im2)


im.show()
im2.show()
