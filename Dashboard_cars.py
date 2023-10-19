import pandas as pd
import numpy as np
import plotly.express as px
import dash as dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

# Importando os dados
cars=pd.read_csv('cars.csv')

# Criando o gráfico
fig = px.bar(cars.groupby('Country').size().nlargest(10).reset_index(name='Count'), x='Country', y='Count', color='Country', title='Top 10 Países com mais carros vendidos')
#vamos fazer um grafico em pizza para ver a distribuição dos cartoes de credito
fig2 = px.pie(cars.groupby('Credit Card Type').size().nlargest(10).reset_index(name='Count'), values='Count', names='Credit Card Type', title='Distribuição dos cartões de crédito usados')
# Criando o app
app = dash.Dash(__name__)
app.title = 'Dashboard Cars'
app.layout = html.Div([
html.Div(children='''Dashboard sobre venda de carros.'''),
dcc.Graph(id='graph-with-slider', figure=fig),
dcc.Graph(id='graph-with-slider2', figure=fig2),
] )





if __name__ == '__main__':
    app.run_server(debug=True)

