from dash import html, dcc, callback, Input, Output, State, no_update, page_registry

sections = html.Nav(id='container_section', children=[
    *[
        dcc.Link(page['name'], href=page['path'], className='link_section')
        for page in page_registry.values()
    ],
    html.A(
        children='Contact', 
        href='https://cristianarboleda.onrender.com/', 
        className='link_section',
        target='_blank',
    )
])

theme = html.Div(
    id='container_theme',
    children=[
        dcc.Dropdown(
            options=[
                {'label': 'EN', 'value': 'EN'},
                {'label': 'ES', 'value': 'ES'},
            ],
            value='EN',
            clearable=False,
            style={'color': 'black',}
        ),
        html.Button(
            id='btn_theme',
            children=html.Img(
                src='/assets/images/sun.png',
                id='img_theme',
            )
        ),
    ]
)
menu = html.Div(id='menu', children=[
    html.Link(rel='stylesheet', href='assets/css/style.css'),
    sections,
    theme,
])

@callback(
    Output('img_theme', 'src'),
    Input('btn_theme', 'n_clicks'),
    State('img_theme', 'src'),
    prevent_initial_call=True,
)

def update_theme(btn_theme, src_theme):
    if not btn_theme:
        return no_update
    
    img_sun = '/assets/images/sun.png'
    img_moon = '/assets/images/moon.png'
    
    if src_theme == img_sun:
        img = img_moon
    
    if src_theme == img_moon:
        img = img_sun
    
    return img
