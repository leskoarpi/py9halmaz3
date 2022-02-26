'''
3. Feladat
A megadott halmazok alapján a program értékelje ki, és az eredményt jelenítse meg a képernyőn az alábbiakat vizsgálva:
- hány olyan étel van, amit mind a két gyerek szeret, és melyek ezek,
- melyek azok az ételek, amiket Peti szeret, de Kriszti nem,
- melyek azok az ételek, melyeket csak egyikük szeret!
'''
Peti_kedvencei = {'halászlé', 'bécsi szelet', 'bukta', 'rakott krumpli', 'almás rétes' }

Kriszti_kedvencei = {'borsóleves', 'bécsi szelet', 'túrós tészta', 'lecsó', 'almás rétes' }

mind2szereti = set(Peti_kedvencei & Kriszti_kedvencei)
print(f'{len(mind2szereti)} olyan etel van amit mind a ketten szeretnek,és ezek azok: \n {mind2szereti}')
print()
csakpeti = set(Peti_kedvencei ^ Kriszti_kedvencei)
print(f'csak peti szereti ezeket az eteleket:\n {csakpeti}')
print()
csakkriszti = set(Kriszti_kedvencei ^ Peti_kedvencei )
print()
egyszereti = set(csakpeti | csakkriszti)
print(f'csak egyikuk szereti ezeket az eteleket: {egyszereti}')