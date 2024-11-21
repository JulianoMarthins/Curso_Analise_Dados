import plotly.express as px

dados_x = ['2019', '2020', '2021', '2022']
dados_y = [10, 5, 15, 10]

fig = px.line(x=dados_x, y=dados_y)

fig.show()
