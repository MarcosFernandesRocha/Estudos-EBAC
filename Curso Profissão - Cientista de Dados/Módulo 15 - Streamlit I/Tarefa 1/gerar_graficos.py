import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os


sns.set()

def plot_pivot_table(df: pd.DataFrame, value: str, index: str, func: str, ylabel: str, xlabel: str, opcao: str='nada'
                    ) -> None:
    if opcao == 'nada':
        pd.pivot_table(data=df, values=value, index=index, aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(data=df, values=value, index=index,aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(data=df,values=value,index=index,aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    st.pyplot()
    return None

st.set_page_config(page_title = 'SINASC Rondônia', 
                    page_icon = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9abbQzsFZeLwGdUA1bECfLnUEZ63HUugIRg&s',
                    layout='wide')

st.write('# Análise SINASC Rondôdia de 2019')

sinasc = pd.read_csv('./input/SINASC_RO_2019.csv')

datas = sinasc['DTNASC'].unique().sort()
sinasc['DTNASC'] = pd.to_datetime(sinasc['DTNASC'])

min_data = sinasc['DTNASC'].min()
max_data = sinasc['DTNASC'].max()

st.write(min_data)
st.write(max_data)

data_inicial = st.sidebar.date_input('Data inicial',
                value = min_data,
                min_value = min_data,
                max_value = max_data)

data_final = st.sidebar.date_input('Data final',
                value = min_data,
                min_value = min_data,
                max_value = max_data)

st.write('Data inicial = ', data_inicial)
st.write('Data final = ', data_final)

sinasc = sinasc[(sinasc['DTNASC'] <= pd.to_datetime(data_final)) & (sinasc['DTNASC'] >= pd.to_datetime(data_inicial))]

st.write(sinasc)
st.write(sinasc.shape)

plot_pivot_table(df=sinasc, value='IDADEMAE', index='DTNASC', func='count', ylabel='Quantidade de nascimentos', xlabel='Data de nascimento')
plot_pivot_table(df=sinasc, value='IDADEMAE', index=['DTNASC', 'SEXO'], func='mean', ylabel='Média da idade das mães', xlabel='Data de nascimento', 
                     opcao='unstack')
plot_pivot_table(df=sinasc, value='PESO', index=['DTNASC', 'SEXO'], func='mean', ylabel='Média do peso dos bebês', xlabel='Data de nascimento',
                     opcao='unstack')
plot_pivot_table(df=sinasc, value='APGAR1', index='ESCMAE', func='median', ylabel='Mediana do APGAR1', xlabel='Escolaridade',
                     opcao='sort')
plot_pivot_table(df=sinasc, value='APGAR1', index='GESTACAO', func='mean', ylabel='Média do APGAR1', xlabel='Gestação',opcao='sort')
plot_pivot_table(df=sinasc, value='APGAR5', index='GESTACAO', func='mean', ylabel='Média do APGAR5', xlabel='Gestação', opcao='sort')


    

    