import piexif
from PIL import Image
import os

# Read image
# Bild importieren
a = input('Geben Sie Bildname: ')
img = Image.open(a)
exif_dict = piexif.load(img.info['exif'])                   # print out all image's information
print(exif_dict)

altitude = exif_dict['GPS'][piexif.GPSIFD.GPSAltitude]
print(altitude)

brand = exif_dict['0th'][306]                 # call out and change apple to samsung
print(brand)

altitude = exif_dict['GPS'][piexif.GPSIFD.GPSAltitude] = (140,1)
exif_new_image = piexif.dump(exif_dict)                     # return exif data as bytes

img.save(a, exif=exif_new_image)                            # save changed to image

brandnew = exif_dict['0th'][271]
print(brandnew)
print(exif_dict)
