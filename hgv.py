


from PIL import Image

img = Image.open(r"D:\sagf.jpg")


img1 = img.convert("L")
img1.show()


img2 = img.convert("1")
img2.show()
