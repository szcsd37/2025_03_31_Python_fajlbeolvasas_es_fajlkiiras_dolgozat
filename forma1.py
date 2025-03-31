"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

adatok = []

nevek_szama = 0

with open("beolvasando_adatok/f1.txt", "r", encoding="utf-8") as forras:
    for sor in forras:
        nev, csapat, gyozelmek_szama, telj_futamok_szama = sor.strip().split(";")
        # print(nev, csapat, gyozelmek_szama, telj_futamok_szama)
        adatok.append([nev, csapat, int(gyozelmek_szama), int(telj_futamok_szama)])

for sor in adatok:
    nevek_szama += 1    

max_verseny = max(adatok, key=lambda x: x[2])

max_teljesitett = max(adatok, key=lambda x: x[3])

telj_versenyek_lista = []

for sor in adatok:
    telj_verseny_szam = int(sor[3])
    telj_versenyek_lista.append(telj_verseny_szam)

print(telj_versenyek_lista)




        





with open("kiirt_adatok/statisztika.txt", "w", encoding="utf-8") as kiiras:
    print(f"A beolvasott fájlban összesen {nevek_szama} versenyző szerepel.", file = kiiras)
    print(f"A legtöbb futamot nyert versenyző: {max_verseny[0]}", file = kiiras)
    print(f"A legtöbb futamot teljesített versenyző: {max_teljesitett[0]} ", file = kiiras)
    print("Az átlagos futamszám: ", sum(telj_versenyek_lista) / len(telj_versenyek_lista), file = kiiras)