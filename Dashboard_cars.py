import pandas as pd
import numpy as np
import plotly.express as px
import dash as dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

# Importando os dados
cars=pd.read_csv('cars.csv')
modelos=cars[['Car Model','Car Brand']].value_counts().head(10).reset_index(name='Count')

# Criando o gráfico
fig = px.bar(cars.groupby('Country').size().nlargest(10).reset_index(name='Count'), x='Country', y='Count', color='Country', title='Top 10 Países com mais carros vendidos')
#vamos fazer um grafico em pizza para ver a distribuição dos cartoes de credito,onde serao destacados os 3 primeiros, e os demais serao agrupados em outros
fig2 = px.pie(cars.groupby('Credit Card Type').size().nlargest(5).reset_index(name= 'Count'), values='Count', names='Credit Card Type', title='Distribuição dos métodos de pagamento')
#vamos fazer um gráfico de frequencia para ver a distribuição dos carros vendidos
fig4 = px.histogram(cars.groupby('Car Brand').size().nlargest(10).reset_index(name='Count'), x='Car Brand',y='Count',color='Count', title='Distribuição das marcas de  carros vendidos')
fig5 = px.bar(cars.groupby('Car Model').size().nlargest(10).reset_index(name='Count'), x='Car Model',y='Count', title='Distribuição dos modelos de carros mais vendidos')
# Criando o app

app = dash.Dash(__name__)
app.title = 'Dashboard Cars'
app.layout = html.Div([
html.Div(children='''Dashboard sobre venda de carros.'''),
dcc.Graph(id='graph-with-slider', figure=fig),
dcc.Graph(id='graph-with-slider2', figure=fig2),
dcc.Graph(id='graph-with-slider4', figure=fig4),
dcc.Graph(id='graph-with-slider5', figure=fig5)

] )





if __name__ == '__main__':
    app.run_server(debug=True)

