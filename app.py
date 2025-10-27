from dash import Dash, html, page_container
from menu import * 

app = Dash(__name__, use_pages=True)

app.layout = html.Div(
    id='main',
    children=[
    menu,
    page_container,
    ]
)

app.run(debug=True, port=8050)