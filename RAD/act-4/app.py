#nivel facil
#adicionar na sidebar
categoria = st.sidebar.selectbox(
    "Categoria salarial",
    options=["Todas"] + list(df["categoria_salario"].unique())
)
#atualizar filtros
#nivel medio
import plotly.express as px

#substituir:
col1.bar_chart(media_cidade)


#por:
fig1 = px.bar(
    df_filtrado,
    x="cidade",
    y="salario",
    color="categoria_salario",
    title="Salário por cidade",
    hover_data=["nome", "idade"]
)

col1.plotly_chart(fig1, use_container_width=True)


#substituir o segundo gráfico:
fig2 = px.bar(
    df_filtrado,
    x="categoria_salario",
    color="categoria_salario",
    title="Distribuição por categoria"
)

col2.plotly_chart(fig2, use_container_width=True)

#nivel dificil
#substituir o bloco upload inteiro por este:
st.sidebar.subheader("📂 Upload de CSV")

uploaded_file = st.sidebar.file_uploader("Envie um CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # limpeza automática
    if "idade" in df.columns:
        df["idade"] = df["idade"].fillna(df["idade"].mean())

    if "salario" in df.columns:
        df["salario"] = df["salario"].fillna(df["salario"].median())

    # features
    if "salario" in df.columns:
        df["salario_anual"] = df["salario"] * 12

        df["categoria_salario"] = df["salario"].apply(
            lambda x: "Alto" if x > 4500 else "Médio" if x > 3000 else "Baixo"
        )

    if "data_contratacao" in df.columns:
        df["data_contratacao"] = pd.to_datetime(df["data_contratacao"])
        df["ano_contratacao"] = df["data_contratacao"].dt.year