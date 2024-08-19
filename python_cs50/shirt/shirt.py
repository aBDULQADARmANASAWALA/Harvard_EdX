from PIL import Image, ImageOps
from sys import argv, exit

if len(argv) != 3:
    print("Invalid command-line arguments")
    exit(1)
for i in [".png", ".jpg", ".jpeg"]:
    if argv[1].endswith(i) and argv[2].endswith(i):
        break
else:
    exit(2)

try:
    with Image.open(argv[1]) as img:
        img = ImageOps.fit(img, (600,600))
        img2 = Image.open("shirt.png")
        img.paste(img2, img2)
        img.save(argv[2])
except FileNotFoundError:
    exit(3)
