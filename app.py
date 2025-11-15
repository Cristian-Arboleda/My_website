from dash import Dash, html, page_container

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)



from menu import * # Se importa este modulo despues de haber activador use_pages

app.layout = html.Div(
    id='main',
    children=[
    menu,
    page_container,
    ]
)

if __name__ == '__main__':
    app.run(debug=True, port=8050)