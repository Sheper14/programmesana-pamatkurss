# Koda lauzējs

Vienkārša Python spēle, kurā dators mēģina uzminēt iedomātu skaitli no 1 līdz 100. Tas izmanto bināro meklēšanu – katrā gājienā pārbauda vidējo skaitli un samazina iespējamo variantu skaitu.

## Kā palaist

Nepieciešams Python 3. Terminālī ievadi:

```bash
python main.py
```

## Kā spēlēt

Iedomājies skaitli un uz datora minējumiem atbildi ar:

- **L** – mans skaitlis ir lielāks.
- **M** – mans skaitlis ir mazāks.
- **U** – skaitlis ir uzminēts.

Ja atbildes ir pareizas, dators skaitli atrod ne vairāk kā 7 gājienos. Ja atbildes ir pretrunīgas, programma par to paziņo.

## Faili

- `main.py` – spēles norise un atbilžu pārbaude.
- `engine.py` – minējumu aprēķināšana un robežu maiņa.
- `testi.md` – programmas pārbaudes.
