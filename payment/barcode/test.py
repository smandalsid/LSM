import cv2
from pyzbar.pyzbar import decode

def reader(img):
    img=cv2.imread(img)
    barcode=decode(img)
    if not barcode:
        print("No barcode detected")
    else:
        for b in barcode:
            if b.data!="":
                # print(b.data.decode())
                return b.data.decode()

# imgs=["barcode/1.JPG", "barcode/2.jpeg",  "barcode/bct.jpeg"]
# for i in imgs:
#     reader(i)