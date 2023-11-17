import dash 
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Carrega os dados do PIB per capita por país e ano
df = pd.read_csv('pib_capta.csv')


# Vamos filtrar o dtaset para retirar a coluna 'Country Code' e 'Indicator Name'
df2=df.drop(['Country Code', 'Indicator Name','Country Code'], axis=1, inplace=True)

# Vamos criar uma coluna com a média do PIB per capita por país
df['Media']=df.mean(axis=1)

# Vamos criaar um grafico com a evolução da media do PIB per capita por país
fig = px.line(df, x='Country Name', y='Media', title='Média do PIB per capita por país')








# Cria um gráfico de mapa de calor com base nos dados do PIB per capita


# Exibe o gráfico

#Criando o Dash
app = dash.Dash(__name__)
app.title = 'Dashboard PIB per capita'
app.layout = html.Div([
html.Div(children='''Dashboard sobre PIB per capita.''')
] )

if __name__ == '__main__':
    app.run_server(debug=True)

