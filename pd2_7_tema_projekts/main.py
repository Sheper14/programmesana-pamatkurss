from engine import aprekinat_minejumu, atjaunot_robezas

apaksa = 1
augsa = 100
gajieni = 0
uzminets = False

print("Iedomājies skaitli no 1 līdz 100.")

while apaksa <= augsa:
    minejums = aprekinat_minejumu(apaksa, augsa)
    gajieni += 1

    atbilde = input(f"Vai tavs skaitlis ir {minejums}? (L/M/U): ")
    atbilde = atbilde.strip().lower()
    while atbilde not in ["l", "m", "u"]:
        atbilde = input("Atbildi ar L, M vai U: ").strip().lower()

    if atbilde == "u":
        uzminets = True
        break

    apaksa, augsa = atjaunot_robezas(apaksa, augsa, minejums, atbilde)

if uzminets:
    print(f"Uzvara {gajieni} gājienos!")
    print("Lineārā meklēšana sliktākajā gadījumā prasītu 100 gājienus.")
else:
    print("Pretruna! Tavas atbildes nevar būt patiesas.")
