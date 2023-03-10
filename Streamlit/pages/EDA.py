import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pprint
import koreanize_matplotlib
import altair as alt
from PIL import Image


st.set_page_config(
    page_title="Agriculture",
    page_icon="πΎ",
    layout="wide",
)

file = 'AgriMarket.csv'

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

df = load_data(file)
df.columns = ["YMD","YM","MD","Product","Price","Cereals","Food Price Index","item_CPI","item_PPI","μ½κΈλ¦¬(μ°%)","νμ¨(μ/US$"]

st.header(" πΎ Agricultural Products Price Prediction")

st.markdown("""       """)
# st.dataframe(df)

st.markdown("## β νλͺ©λ³ EDA")
st.markdown("")
tab1, tab2, tab3, tab4 = st.tabs(["π§ λ§λ","π₯ κ°μ", "π κ³ κ΅¬λ§", "π κΉ»μ" ])

with tab1:
    df_g = df[df["Product"] == "λ§λ"]
    df_g["M"] = df_g['MD'].map(lambda x:str(x)[:-2])
    df_g["Y"] = df_g['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_g.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_g.groupby('M')['Price'].sum())
          
    plt.figure(figsize=(20, 7))
    st.markdown("")
    st.markdown("π‘Β 9 ~ 10μμ μ¬μ΄μ 5 ~ 6μμ μν")
    gh1 = px.line(data_1, title = "κ°κ²© μΆμΈμ ")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "κ³μ λ³ κ°κ²©")
    st.plotly_chart(gh2)

with tab2:
    df_p = df[df["Product"] == "κ°μ"]
    df_p["M"] = df_p['MD'].map(lambda x:str(x)[:-2])
    df_p["Y"] = df_p['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_p.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_p.groupby('M')['Price'].sum())


    st.markdown("- λ΄κ°μ:  2 ~ 4μ μ¬μ΄μ μ¬μ΄μ ")
    st.markdown("- κ°μκ°μ: 8μλ§κΉμ§ μ¬μ΄μ ")
    st.markdown("** μ§μ­λ³λ‘ 90 ~ 100 μΌ μ λμ¬λ°° ν μν ** ")
    gh1 = px.line(data_1, title = "κ°κ²© μΆμΈμ ")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "κ³μ λ³ κ°κ²©")
    st.plotly_chart(gh2)

with tab3:
    df_sp = df[df["Product"] == "κ³ κ΅¬λ§"]
    df_sp["M"] = df_sp['MD'].map(lambda x:str(x)[:-2])
    df_sp["Y"] = df_sp['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_sp.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_sp.groupby('M')['Price'].sum())


    plt.figure(figsize=(20, 7))
    sns.lineplot(data=df_sp, x="M", y=df_sp["Price"])
    st.markdown("κ°μ~κ²¨μΈ μ¨λκ° λ?μμ§μλ‘ μμμ¦κ° (κ΅°κ³ κ΅¬λ§) + μ¬λ¦ μ΄μκΈ°μ¨ λ§μμλ‘ κ³΅κΈκ°μ ")
    gh1 = px.line(data_1, title = "κ°κ²© μΆμΈμ ")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "κ³μ λ³ κ°κ²©")
    st.plotly_chart(gh2)

with tab4:
    df_k = df[df["Product"] == "κΉ»μ"]
    df_k["M"] = df_k['MD'].map(lambda x:str(x)[:-2])
    df_k["Y"] = df_k['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_k.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_k.groupby('M')['Price'].sum())
  
    st.markdown("π‘Β 4~5μμ μ¬μ΄μ λ΄μλ 4-50μΌ, μ¬λ¦ νμ’μ 40μΌ ν μν")
    gh1 = px.line(data_1, title = "κ°κ²© μΆμΈμ ")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "κ³μ λ³ κ°κ²©")
    st.plotly_chart(gh2)




st.markdown("")
st.markdown("---")
st.markdown("")