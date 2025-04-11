# Labb 2 – G-nivå – anpassad för brett format (Tabell 1A)
import pandas as pd
import plotly.graph_objects as go
import os

# Skapa mapp om den inte finns
if not os.path.exists("visualiseringar"):
    os.makedirs("visualiseringar")

# Läs in datan från rad 7 (där själva tabellen börjar)
df = pd.read_excel("betyg_o_prov_riksnivå.xlsx", sheet_name="Tabell 1A", skiprows=6)

# Byt namn på kolumn 'Unnamed: 0' till 'Läsår'
df = df.rename(columns={'Unnamed: 0': 'Läsår'})

# Ta bort rader där Läsår saknas
df = df[df['Läsår'].notna()]

# Välj endast rader för "Andel elever som saknar godkänt betyg..."
df_andel = df.iloc[0:6]  # Första 6 raderna = Andel utan godkänt
df_merit = df.iloc[13:19]  # Meritvärde ligger oftast lite längre ner

# UPPGIFT 2a – Andel utan godkänt betyg
fig1 = go.Figure()

for kol in ['Totalt', 'Flickor', 'Pojkar']:
    fig1.add_trace(go.Scatter(
        x=df_andel['Läsår'],
        y=df_andel[kol],
        mode="lines+markers",
        name=kol
    ))

fig1.update_layout(
    title="Andel elever utan godkänt betyg",
    xaxis_title="Läsår",
    yaxis_title="Andel (%)",
    template="plotly_white"
)

fig1.write_html("visualiseringar/andel_utan_godkant.html")

# UPPGIFT 2b – Meritvärde
fig2 = go.Figure()

for kol in ['Totalt', 'Flickor', 'Pojkar']:
    fig2.add_trace(go.Scatter(
        x=df_merit['Läsår'],
        y=df_merit[kol],
        mode="lines+markers",
        name=kol
    ))

fig2.update_layout(
    title="Meritvärde för elever",
    xaxis_title="Läsår",
    yaxis_title="Meritvärde",
    template="plotly_white"
)

fig2.write_html("visualiseringar/meritvärde.html")
