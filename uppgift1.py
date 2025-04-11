# Labb 2 – Uppgift 1 – G-nivå
import pandas as pd
import matplotlib.pyplot as plt
import os

# Skapa visualiseringsmapp om den inte finns
if not os.path.exists("visualiseringar"):
    os.makedirs("visualiseringar")

# Läs in Excel-filen
filnamn = "riket2023_åk9_np.xlsx"
eng = pd.read_excel(filnamn, sheet_name="Engelska")
ma = pd.read_excel(filnamn, sheet_name="Matematik")
sve = pd.read_excel(filnamn, sheet_name="Svenska")
svas = pd.read_excel(filnamn, sheet_name="Svenska som andraspråk")

# Kolumnnamn enligt instruktion
kol_namn = [
    "Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)",
    "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)",
    "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"
]

# Sätt kolumnnamn
for df in [eng, ma, sve, svas]:
    df.columns = kol_namn

# Inställningar för grafer
ämnen = ["Engelska", "Matematik", "Svenska", "Svenska som andraspråk"]
data = [eng, ma, sve, svas]
positioner = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Skapa subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Totalt poäng i olika ämnen – jämförelse mellan huvudmän", fontsize=14)

for ämne, df, pos in zip(ämnen, data, positioner):
    ax = axs[pos[0]][pos[1]]

    # Filtrera bort rader med saknade eller felaktiga värden
    df = df[df["Huvudman"].apply(lambda x: isinstance(x, str))]
    df = df[pd.to_numeric(df["Totalt (poäng)"], errors="coerce").notnull()]

    huvudmän = df["Huvudman"]
    poäng = df["Totalt (poäng)"]

    ax.bar(huvudmän, poäng, color="skyblue")
    ax.set_title(ämne)
    ax.set_ylabel("Poäng")
    ax.set_xlabel("Huvudman")
    ax.set_xticklabels(huvudmän, rotation=45)

# Spara och visa
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig("visualiseringar/np_totalt_poäng.png")
plt.show()
