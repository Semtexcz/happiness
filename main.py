import matplotlib.pyplot as plt

import pandas as pd

# Data pro tabulku na základě rešerše
data = {
    "Činnost": [
        "Sex / Intimní aktivity",
        "Společenské aktivity (socializace)",
        "Relaxace a odpočinek",
        "Fyzická aktivita (cvičení)",
        "Jídlo",
        "Dobrovolnictví a péče o druhé",
        "Duchovní aktivity",
        "Hobby a koníčky",
        "Pití alkoholu / Party",
        "Nakupování pro radost",
        "Hraní videoher",
        "Placená práce",
        "Studium / školení",
        "Domácí práce",
        "Dojíždění",
        "Osobní hygiena",
        "Být nemocný",
        "Používání sociálních sítí"
    ],
    "Zábavnost (1-10)": [10, 9, 8, 9, 8, 6, 5, 7, 9, 7, 8, 4, 3, 2, 1, 2, 1, 2],
    "Smysluplnost (1-10)": [10, 8, 5, 7, 5, 10, 9, 7, 4, 3, 4, 8, 9, 4, 2, 3, 1, 1]
}

# Vytvoření DataFrame
df = pd.DataFrame(data)

# Výpočet celkového skóre jako součet zábavnosti a smysluplnosti
df["Celkové skóre"] = df["Zábavnost (1-10)"] + df["Smysluplnost (1-10)"]

# Seřazení podle celkového skóre (sestupně)
df_sorted = df.sort_values(by="Celkové skóre", ascending=False)

# # Zobrazení tabulky
# import ace_tools as tools
# tools.display_dataframe_to_user(name="Hodnocení činností", dataframe=df_sorted)

# Velikost bodů podle celkového skóre
sizes = df["Celkové skóre"] * 10  # Násobíme pro lepší vizualizaci

# Barvy bodů: prvních 6 činností zeleně, posledních 6 červeně, ostatní modře
colors = ['green'] * 6 + ['blue'] * (len(df) - 12) + ['red'] * 6

# Zkrácené popisky pro lepší čitelnost
short_labels = [
    "Sex", "Socializace", "Relax", "Cvičení", "Jídlo",
    "Dobrovolnictví", "Duchovní akt.", "Hobby", "Party", "Nakupování",
    "Hraní her", "Práce", "Studium", "Domácí práce", "Dojíždění",
    "Hygiena", "Nemoc", "Sociální sítě"
]

# Vytvoření bodového grafu s upravenými barvami a značkami
plt.figure(figsize=(10, 6))

# Vykreslení bodů s různými barvami
plt.scatter(df["Smysluplnost (1-10)"], df["Zábavnost (1-10)"], s=sizes, c=colors, alpha=0.7)

# Přidání popisků bodů s offsetem pro čitelnost
for i, txt in enumerate(short_labels):
    plt.annotate(txt, (df["Smysluplnost (1-10)"][i], df["Zábavnost (1-10)"][i]), fontsize=9, alpha=0.8,
                 textcoords="offset points", xytext=(5,5), ha='left')

# Nastavení os a názvů
plt.xlabel("Smysluplnost (1-10)")
plt.ylabel("Zábavnost (1-10)")
plt.title("Bodový graf: Smysluplnost vs. Zábavnost činností (velikost značky = celkové skóre)")
plt.grid(True)

# Uložení grafu jako obrázek (např. PNG)
plt.savefig("graf.png", dpi=300, bbox_inches='tight')

# Zobrazení grafu
plt.show()
