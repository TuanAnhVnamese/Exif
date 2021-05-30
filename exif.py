from exif import Image          
import os
from fractions import *


#                                                              Bild importieren
try:
    dir_file = input('Geben Sie Ort des Bildes: ')
    bild_name = input('Geben Sie Name von Bild: ')
    the_dir = dir_file + '/' + bild_name
    with open(the_dir, "rb") as myimage_file:
        myimage = Image(myimage_file)




# **********************************************************************************************************
# **********************************************************************************************************
#                                               Informationen

    def getformat(path):                                                                    # Format
        from PIL import Image
        img = Image.open(path)
        return img


    def get_date_time(path):                                                                # Zeit
        try:
            time = path.datetime
            return time
        except:
            return None

    def get_aperture_value(path):                                                           # Blende
        try:
            aperture = path.aperture_value
            return aperture
        except:
            return None

    def get_exposure_time(path):                                                           # Belichtungszeit
        try:
            return path.exposure_time
        except:
            return None

    def get_focal_length(path):                                                             # Brennweite
        try:
            focal_length = path.focal_length
            return focal_length
        except:
            return None

    def get_iso(path):                                                                      # ISO-Werte nicht veränderbar
        from PIL import Image
        import piexif
        try:
            img = Image.open(path)
            exif_dict = piexif.load(img.info['exif'])
            iso = exif_dict['Exif'][34855]
            if isinstance(iso, tuple):
                iso_list = list(iso)
                for index, value in enumerate(iso_list):
                    iso_list[index] = value-48                                              # Wenn Iso-wert durch Benutzer verändern wird, Iso-wert wird als tuple gespeichert. Bsp wenn wir iso nach 100 umwandeln, dann exif wird so (49, 48, 48) gespeicher.
                iso = tuple(iso_list)                                                       # ich hab Regel gefunden, 48 entspricht 0, 49 = 1, ... 57 entspricht 9.
                iso_int = int(''.join(map(str, iso)))                                       # tuple nach integer umwandeln
                return iso_int
            else:
                return iso
        except:
            return None
        img.close()

    def get_flash(path):                                                                    # Blitzinformation nicht veränderbar
        from PIL import Image
        try:
            flash = Image.open(path)._getexif()[37385]
            if flash is True:
                return 'Blitz benutzt'
            else:
                  return 'Kein Blitz'''
        except:
            return 'Kein Blitz'

                                                    # Informationen zum Fotografieren:

    def get_make(path):                                                                         # Marke
        try:
            make = path.make
            return make
        except:
            return 'Unbekannt'

    def get_model(path):                                                                         # Model
        try:
            model = path.model
            return model
        except:
            return 'Unbekannt'

    def get_lens_model(path):                                                                     # Lens Model
        try:
            lens_model = path.lens_model
            return lens_model
        except:
            return 'Unbekannt'

    def get_sea_level(path):                                                                        # Meer level
        try:
            sea_level = path.gps_altitude
            return sea_level
        except:
            return 'Unbekannt'

    def get_latitude(path):                                                                         # Breitengrad
        try:
            print(f'Breitengrad: \t\t\t\t\t {path.gps_latitude} {path.gps_latitude_ref}')
        except:
            return 'Unbekannt'

    def get_longitude(path):
        try:
            print(f'Längengrad: \t\t\t\t\t {path.gps_longitude} {path.gps_longitude_ref}')            # Längengrad
        except:
            return 'Unbekannt'


    # **********************************************************************************************************
    # **********************************************************************************************************
    #                                               Ausdruck

    print('Exif von Gruppe 4: \t\t\t\t Version 1.0')                    # Version
    print(f'Ort des Bildes: \t\t\t\t {the_dir}')                        # Ort

    print(f'Format: \t\t\t\t {getformat(the_dir).format}')           # Format and Mode können nicht veränderbar sein
    print(f'Mode: \t\t\t\t\t {getformat(the_dir).mode}')

    if get_date_time(myimage) == None:                                             # Zeit
        print(f'Erstellte Zeit: \t\t\t\t Unbekannt')
    else:
        print(f'Erstellte Zeit: \t\t\t\t {get_date_time(myimage)}')

    if get_aperture_value(myimage) == None:                                             # Blende
        print(f'Blende: \t\t\t\t Unbekannt')
    else:
        print(f'Blende: \t\t\t\t {round(float(get_aperture_value(myimage)), 1)}')

    if get_exposure_time(myimage)==None:                                                # Belichtungszeit
        print(f'Belichtungszeit: \t\t\t\t Unbekannt')
    else:
        print(f'Belichtungszeit: \t\t\t\t {Fraction((get_exposure_time(myimage))).limit_denominator(100000)}')

    if get_focal_length(myimage) == None:                                               # Brennweite
        print(f'Brennweite: \t\t\t\t\t Unbekannt')
    else:
        print(f'Brennweite: \t\t\t\t\t {get_focal_length(myimage)} mm')

    if get_iso(the_dir) == None:                                                         # Iso-Werte nicht veränderbar
        print(f'ISO Werte: \t\t\t\t Unbekannt')
    else:
        print(f'ISO Werte: \t\t\t\t {get_iso(the_dir)}')

    print(f'Blitzinformation: \t\t\t\t {get_flash(the_dir)}')                             # Blitz nicht veränderbar

    print(f'Marke: \t\t\t\t\t {get_make(myimage)}')                                   # Marke

    print(f'Model: \t\t\t\t\t {get_model(myimage)}')                                   # Model

    print(f'Lens des Kameras: \t\t\t\t {get_lens_model(myimage)}')                         # Lens des Kameras

    print(f'Meer Level: \t\t\t\t\t {get_sea_level(myimage)} m Über dem Meeresspiegel ')    # Meer level

    get_latitude(myimage)

    get_longitude(myimage)

    print('\n')
    # **********************************************************************************************************
    # **********************************************************************************************************
    #                                               Änderungsfunktionen


    def namechange(path, path1):                                                                           # Name ändern
        b = input('Geben neue Name an: ')
        os.rename(os.path.join(path), os.path.join(dir_file + '/' + b))
        the_dir_new = path1 + '/' + b
        return the_dir_new

    def timechange(path, myimage):                                                                  # Zeit ändern
        myimage.datetime = str(input('Geben Sie neue Zeit, bitten Folgen Sie in Format: jj/mm/tt Stunde:Minute:Sekunde: '))
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def aperturechange(path, myimage):                                                              # Blende ändern
        myimage.aperture_value = float(input('Geben Sie neuen Blendenwert: '))
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def exposurechange(path, myimage):
        myimage.exposure_time = str(input('Geben Sie neue Belichtungszeit: '))                  # Belichtungszeit ändern
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def focal_lengthchange(path, myimage):                                                              # Brennweite ändern
        myimage.focal_length = float(input('Geben Sie neue Brennweite: '))
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def makerchange(path, myimage):
        myimage.make = input('Geben Sie neue Marke: ')                                         # Marke ändern
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def modelchange(path, myimage):
        myimage.model = input('Geben Sie neue Model: ')                                         # Model ändern
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def lenschange(path, myimage):
        myimage.lens_model = input('Geben Sie neu Lens des Kameras: ')                      # Lens Kameras ändern
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def levelchange(path, myimage):
        myimage.gps_altitude = input('Geben Sie neues Meer Level: ')                            # Meer Level ändern
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def latitudechange(path, myimage):
        print('Geben Sie neu Breitengrad: ')
        myimage.gps_latitude = (input('1. Breitengrad: '), input('2. Breitengrad: '), input('3. Breitengrad: '))   # Breitengrad ändern
        myimage.gps_latitude_ref = input('Geben Sie neu Breitengrad-Referenz: ')
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def longitudechange(path, myimage):
        print('Geben Sie neu Längegrad: ')
        myimage.gps_longitude = (input('1. Längengrad: '), input('2. Längengrad: '), input('3. Längengrad: '))  # Längengrad ändern
        myimage.gps_longitude_ref = input('Geben Sie neu Längengrad-Referenz: ')
        with open(path, "wb") as a_update:
            a_update.write(myimage.get_file())

    def isochange(path):
        from PIL import Image
        import piexif
        img = Image.open(path)
        exif_dict = piexif.load(img.info['exif'])
        exif_dict['Exif'][34855] = input('Geben Sie neuen Iso-wert: ').encode()                                 # Hier brachen wir als byte speichern, dann muss encode() am Ende (string to byte)
        exif_bytes = piexif.dump(exif_dict)                                                                     # Zurück exif als bytes
        img.save(path, exif=exif_bytes)
        img.close()

    # **********************************************************************************************************
    # **********************************************************************************************************
    #                                               Benutzeroberfläche
    wollen = input('Wollen Sie was ändern? j/n: ')
    print('\n')
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
            6.Marke
            7.Model
            8.Lens des Kameras
            9.Meer Level
            10.Breitengrad
            11.Längengrad
            12.Iso-werte
            13.Exit
            ''')
            ans = input('Was wollen Sie machen? ')
            if ans == '1':
                the_dir = namechange(the_dir, dir_file)
                print('\n Name wird sich schon geändert')
            elif ans == '2':
                timechange(the_dir, myimage)
                print('\n Datum und Zeit werden sich schon geändert')
            elif ans == '3':
                aperturechange(the_dir, myimage)
                print('\n Blende wird sich schon geändert')
            elif ans == '4':
                exposurechange(the_dir, myimage)
                print('\n Belichtungszeit wird sich schon geändert ')
            elif ans == '5':
                focal_lengthchange(the_dir, myimage)
                print('\n Brennweiter wird sich schon geändert')
            elif ans == '6':
                makerchange(the_dir, myimage)
                print('\n Marke wird sich schon geändert')
            elif ans == '7':
                modelchange(the_dir, myimage)
                print('\n Model wird sich schon geändert')
            elif ans == '8':
                lenschange(the_dir, myimage)
                print('\n Lens des Kameras wird sich schon geändert')
            elif ans == '9':
                levelchange(the_dir, myimage)
                print('\n Meer Level wird sich schon geändert')
            elif ans == '10':
                latitudechange(the_dir, myimage)
                print('\n Breitengrad wird sich schon geändert')
            elif ans == '11':
                longitudechange(the_dir, myimage)
                print('\n Längengrad wird sich schon geändert')
            elif ans == '12':
                isochange(the_dir)
                print('\n Iso-wert wird sich schon geändert')
            elif ans == '13':
                print('\n Ciao!')
                break
            elif ans != '':
                print("\n Nicht gültig!! Bitte Geben Sie wieder Auswahl an ")
    elif wollen == 'n':
        print('Ciao!!')
        input('Drücken Sie eine beliebige Taste, um das Programm zu schließen')

except:
    print('Falsche Name oder Ort!! Bitte neu starten')

input('Drücken Sie eine beliebige Taste, um das Programm zu schließen')












