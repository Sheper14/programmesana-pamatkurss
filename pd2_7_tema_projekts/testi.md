# Programmas testi

Pārbaudīju, vai programma pareizi uzmin skaitli un reaģē uz dažādām atbildēm.

| Tests | Ievadītās atbildes | Rezultāts |
|---|---|---|
| Skaitlis 73 | `L, M, L, L, L, U` | Uzmin 6 gājienos. |
| Skaitlis 1 | `M, M, M, M, M, U` | Uzmin 6 gājienos. |
| Skaitlis 100 | `L, L, L, L, L, L, U` | Uzmin 7 gājienos. |
| Pretrunīgas atbildes | `L, L, M, M, M, M` | Parāda paziņojumu par pretrunu. |
| Nederīga ievade | `q`, pēc tam `U` | Lūdz ievadīt L, M vai U vēlreiz. |
| Atbilde ar atstarpēm | `  u  ` | Pieņem atbildi. |

**Secinājums:** Programma darbojas pareizi – skaitli no 1 līdz 100 var uzminēt ne vairāk kā 7 gājienos, un tiek apstrādātas arī nederīgas vai pretrunīgas atbildes.
