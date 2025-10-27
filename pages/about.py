from dash import register_page, html

register_page(__name__, path='/')

layout = html.Div(
    children=[
        html.Link(rel='stylesheet', href='assets/css/about.css'),
        html.P('hola')
    ]
)