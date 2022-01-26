'''
1.1 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhajtó)

1.2 Feladat
Az előbbi programot módosítsd úgy, hogy újabb és újabb mondatot kérjen be a program (amig a felhasználó csak egy ENTER-t nem üt), majd állapítsa meg, és írja ki mineden egyes alkalommal a mondat fajtáját!
'''

while True:

    beker = input('Írj egy mondatot: ')
    if beker == "":
        break
    if beker[-1] == "?":
        print('Kérdő mondat.')

    if beker[-1] == ".":
        print('Kijelentő mondat')

    if beker[-1] == "!":
        print('Felkiáltó mondat.')

    if beker[-1] == "bárcsak" or "bár" in beker:
        print('Óhajtó mondat.')
 