#nivel 1
import pandas as pd

df = pd.read_csv("livros.csv", sep=";")
df.head()

df.info()
df.describe()
 
df.isnull().sum()

df[df["paginas"] == 0]

df["ano"].value_counts().sort_index()

#nivel 2
df["faixa_paginas"] = df["paginas"].apply(
    lambda x: "Curto" if x < 150 
    else "Médio" if x <= 350 
    else "Longo"
)

df_limpo = df[df["paginas"] > 0].copy()

mediana = df_limpo["ano"].median()

df_limpo["ano"] = df_limpo["ano"].fillna(mediana)
df_limpo["ano"] = df_limpo["ano"].astype(int)

df_limpo["decada"] = (df_limpo["ano"] // 10) * 10
 
#nivel 3
df_limpo.groupby("decada")["paginas"].mean().sort_index()

df_limpo["autor"].value_counts().head(10)

df_limpo[df_limpo["ano"] > 2010]["faixa_paginas"].value_counts()

df_limpo.to_excel("livros_analisados.xlsx", index=False)