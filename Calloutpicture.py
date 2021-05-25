import piexif
from PIL import Image
import os
from fractions import *
#brand test

#                                               Bild importieren

a = input('Geben Sie Bildname: ')
img = Image.open(a)
exif_dict = piexif.load(img.info['exif'])                   # print out all image's information


# **********************************************************************************************************
# **********************************************************************************************************
#                                               Informationen

print(f'Typ:  \t\t\t\t\t\t    {img.format}')                                    # Format

print(f'Mod:  \t\t\t\t\t\t    {img.mode}')                                              # Mode

def get_date_taken(img):                                                               # Date
    exif_dict = piexif.load(img.info['exif'])
    t = str(exif_dict['0th'][306], 'utf-8')
    return t #Image.open(path)._getexif()[36867]
print(f'Ertellte Zeit:  \t\t\t    {get_date_taken(img)}')

def get_aperture_value(path):                                                            # Blende
    return Image.open(path)._getexif()[37378]
print(f'Blende:  \t\t\t\t\t    {round(float(get_aperture_value(a)), 1)}')

def get_exposure_time(path):                                                            # Belichtungszeit
    return Image.open(path)._getexif()[33434]
print(f'Belichtungszeit:  \t\t\t    {Fraction(get_exposure_time(a))}')

def get_focal_length(path):                                                            # Brennweite
    return Image.open(path)._getexif()[37386]
print(f'Brennweite:  \t\t\t\t    {get_focal_length(a)} mm')

def get_iso(path):                                                                      # ISO-Werte
    return Image.open(path)._getexif()[34855]
print(f'ISO Werte:  \t\t\t\t    {get_iso(a)}')

def get_flash(path):                                                                    # Blitzinformation
    if Image.open(path)._getexif()[37385] is True:
        return 'Blitz benutzt'
    else:
        return 'Kein Blitz'
print(f'Blitzinformation:  \t\t\t    {get_flash(a)}')

def get_shutter_speed(path):                                                            # Shutter speed
    return Image.open(path)._getexif()[37377]
print(f'Shutter Speed:  \t\t\t    {round(float(get_shutter_speed(a)), 2)}')

# **********************************************************************************************************
# **********************************************************************************************************
#                                               Änderungsfunktionen

exif_dict = piexif.load(img.info['exif'])
def namechange(a):                                                                      # Name ändern
    b = input('Geben neue Name an: ')
    os.rename(a, b)
    return b

def timechange(a):
    exif_dict['0th'][306] = input('Bitte Format: jj/mm/tt und Stunde:Minute:Sekunde ')
    exif_new_image = piexif.dump(exif_dict)
    img.save(a, exif=exif_new_image)


# **********************************************************************************************************
# **********************************************************************************************************
#                                               Benutzeroberfläche
wollen = input('Wollen Sie was ändern? j/n: ')
if wollen == 'j':
    print('Was wollen Sie ändern? Wählen Sie in der folgenden Liste aus:')
    ans = True
    while ans:
        print('''
        1.Name
        2.Datum und Zeit
        3.Blende
        4.Belichtungszeit
        5.Brennweiter
        6.ISO-Werte
        7.Blitzinformation
        8.Exit
        ''')
        ans = input('Was wollen Sie machen? ')
        if ans == '1':
            namechange(a)
            print('\n Name schon geändert')
        elif ans == '2':
            timechange(a)
            print('\n Datum und Zeit schon geändert')
        elif ans == '3':
            print('\n Blende schon geändert')
        elif ans == '4':
            print('\n Belichtungszeit schon geändert ')
        elif ans == '5':
            print('\n Brennweiter schon geändert')
        elif ans == '6':
            print('\n ISO-Werte schon geändert')
        elif ans == '7':
            print('\n Blitzinformation schon geändert')
        elif ans == '8':
            print('\n Ciao!')
            break
        elif ans != '':
            print("\n Not Valid Choice Try again")
elif wollen == 'n':
    print('End')















