
# Labb 2 – Uppgift 1


import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("visualiseringar"):
    os.makedirs("visualiseringar")

# Läs in data från Excel
filnamn = "riket2023_åk9_np.xlsx"

eng = pd.read_excel(filnamn, sheet_name="engelska")
ma = pd.read_excel(filnamn, sheet_name="matematik")
sve = pd.read_excel(filnamn, sheet_name="svenska")
svas = pd.read_excel(filnamn, sheet_name="svenska som andraspråk")

# Kolumnnamn 
kol_namn = [
    "Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)",
    "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)",
    "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"
]

for df in [eng, ma, sve, svas]:
    df.columns = kol_namn

# Skapa diagram
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Totalt poäng i olika ämnen – jämförelse mellan huvudmän", fontsize=14)

ämnen = ["Engelska", "Matematik", "Svenska", "Svenska som andraspråk"]
data = [eng, ma, sve, svas]
positioner = [(0, 0), (0, 1), (1, 0), (1, 1)]

for i, (ämne, df, pos) in enumerate(zip(ämnen, data, positioner)):
    ax = axs[pos]
    huvudmän = df["Huvudman"]
    poäng = df["Totalt (poäng)"]
    ax.bar(huvudmän, poäng, color="skyblue")
    ax.set_title(ämne)
    ax.set_ylabel("Poäng")
    ax.set_xlabel("Huvudman")
    ax.set_xticklabels(huvudmän, rotation=45)

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig("visualiseringar/np_totalt_poäng.png")
plt.show()
