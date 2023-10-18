#Importando as bibliotecas
import pandas as pd
import numpy as np
import dash as dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output


# Importando os dados
df1=pd.read_excel('Tabela_1_1.xlsx')
df2=pd.read_excel('Tabela_1_2.xlsx')
df3=pd.read_excel('Tabela_1_3.xlsx')
df4=pd.read_excel('Tabela_1_4.xlsx')




# Criando o app
app = dash.Dash(__name__)
app.title = 'Dashboard Empreendedorismo'
app.layout = html.Div([
html.Div(children='''Dash: A web application framework for Python.'''),
dcc.Graph(id='graph-with-slider' )
])

if __name__ == '__main__':
    app.run(debug=True)