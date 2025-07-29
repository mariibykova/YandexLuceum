from PIL import Image
 
 
im = Image.open('image.bmp')
x, y = im.size
for i in range(4):
    for j in range(4):
        im_crop = im.crop((j * int(x / 4), i * int(y / 4),
                           j * int(x / 4) + int(x / 4), i * int(y / 4) + int(y / 4)))
        name = f"{'image'}{i + 1}{j + 1}.bmp"
        if i + j < 6:
            im_crop.save(name)