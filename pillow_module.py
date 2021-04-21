from PIL import Image, ImageEnhance, ImageFilter
import os
# img1 = Image.open("panda.jpg")
# img1.save("panda.png")
# img1.save("panda.pdf")
# img1.show()
# MAX_SIZE = (250, 250)
# img1.thumbnail(MAX_SIZE)
# img1.save("pandasmall.jpg")

# for item in os.listdir():
#     if item.endswith(".jpg"):
#         img1 = Image.open(item)
#         name, ext = os.path.splitext(item)
#         img1.save(f"{name}.png")
img1 = Image.open("panda.jpg")
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(0).save("pandablur.jpg")
# enhancer.enhance(20).save("pandasharp.jpg")

# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(0).save("panda_BW.jpg")
# enhancer.enhance(5).save("pandacolor.jpg")

# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(0).save("pandablack.jpg")
# enhancer.enhance(2).save("pandabright.jpg")

# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(0).save("pandalow.jpg")
# enhancer.enhance(2).save("pandahigh.jpg")

img1.filter(ImageFilter.GaussianBlur(radius=4)).save("blurredpanda.jpg")