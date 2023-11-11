import streamlit as st
import pandas as pd

# Diseño personalizado
df = pd.read_csv('hurto_a_persona_transporte_publico.csv')

#st.table(df.loc[:, "estado_civil"].unique())

estadoCivil = df.loc[:,"cantidad"].unique()

option = st.selectbox('Fecha Hecho',estadoCivil)

st.header(option)

filtroEstadoCivil = df[df["cantidad"] == option]

st.write(filtroEstadoCivil.describe())