import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ── 1. Montagem Simplificada do Dataset ───────────────────────────
np.random.seed(42)

produtos = {
    "Dom Casmurro": ("Literatura", 35.90),
    "Sapiens": ("Ciências", 54.90),
    "Python para Dados": ("Tecnologia", 89.90),
    "Clean Code": ("Tecnologia", 95.00),
    "Atomic Habits": ("Autoajuda", 44.90)
}

nomes_prod = np.random.choice(list(produtos.keys()), 50)

df = pd.DataFrame({
    "data": pd.date_range("2024-01-01", "2024-06-30", periods=50).strftime("%Y-%m-%d"),
    "produto": nomes_prod,
    "categoria": [produtos[p][0] for p in nomes_prod],
    "quantidade": np.random.randint(1, 6, 50),
    "preco_unit": [produtos[p][1] for p in nomes_prod],
    "vendedor": np.random.choice(["Ana", "Carlos", "Bruno", "Fernanda"], 50)
})

df["total_venda"] = df["quantidade"] * df["preco_unit"]


# ── 2. Resolução dos Desafios ──────────────────────────────────────

# D1: Calcular evolução do faturamento mês a mês
print("--- D1: Faturamento Mês a Mês ---")
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month
faturamento_mensal = df.groupby("mes")["total_venda"].sum()
print(faturamento_mensal, "\n")


# D2: Criar um gráfico de linha mostrando a tendência de vendas
# plt.figure(figsize=(8, 4))
plt.plot(faturamento_mensal.index, faturamento_mensal.values, marker='o', linestyle='-', color='b')
plt.title("Tendência de Vendas Mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento Total (R$)")
plt.xticks(faturamento_mensal.index) # Garante que apenas os meses existentes apareçam no eixo X
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# D3: Descobrir qual vendedor tem o maior ticket médio
print("--- D3: Vendedor com Maior Ticket Médio ---")
ticket_medio = df.groupby("vendedor")["total_venda"].mean()
maior_ticket = ticket_medio.sort_values(ascending=False).head(1)
print(maior_ticket, "\n")


# D4: Filtrar vendas > 200 e analisar categorias dominantes
print("--- D4: Categorias com vendas acima de R$200 ---")
vendas_altas = df[df["total_venda"] > 200]
categorias_dominantes = vendas_altas["categoria"].value_counts()
print(categorias_dominantes, "\n")


# D5: Adicionar 5 linhas com nulos, identificá-los e tratá-los
print("--- D5: Tratamento de Nulos ---")
# Criando 5 linhas vazias (nulas) e adicionando ao fim do DataFrame
linhas_nulas = pd.DataFrame([{"data": np.nan, "total_venda": np.nan}] * 5)
df_com_nulos = pd.concat([df, linhas_nulas], ignore_index=True)

print("Quantidade de nulos ANTES do tratamento:")
print(df_com_nulos[["data", "total_venda"]].isnull().sum(), "\n")

# Tratando: removendo qualquer linha que tenha 'total_venda' nulo
df_tratado = df_com_nulos.dropna(subset=["total_venda"])

print("Quantidade de nulos APÓS tratamento com .dropna():")
print(df_tratado[["data", "total_venda"]].isnull().sum())