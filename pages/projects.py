from dash import register_page, html, dcc, callback, Input, Output, State, no_update, ctx

register_page(__name__)

url_img = 'assets/images/project/'
project_data = [
    {
        'title': 'twitch_notificacion_bot', 
        'description': 'A Discord bot developed in Python whose purpose is to automatically notify when a Twitch channel goes live.', 
        'url': 'https://github.com/Cristian-Arboleda/bot_biscuittp_twitch_avisos', 
        'img': 'twitch_notificacion_bot',
        'tools': ['python']
    },
    {
        'title': 'link_in_bio_biscuittp',
        'description': 'A page that displays a brief description about me and gathers all the links to my personal social media profiles.',
        'url': 'https://biscuittp-stream.onrender.com',
        'img': 'link_in_bio_biscuittp',
        'tools': ['python', 'css', 'html', 'dash']
    },
    {
        'title': 'welcome_bot_for_discord',
        'description': 'A Discord bot that welcomes new server members by mentioning their name and displaying a personalized img.',
        'url': 'https://github.com/Cristian-Arboleda/bot-bienvenida',
        'img': 'welcome_bot_for_discord',
        'tools': ['python']
    },
    {
        'title': 'Weight_Progress',
        'description': 'Interactive dashboard that records and visualizes daily weight progress in a database.',
        'url': '',
        'img': '',
        'tools': ['python', 'html', 'css', 'postgresql'],
    },
    {
        'title': 'link_in_bio_cristian',
        'description': 'Interactive dashboard that records and visualizes daily weight progress in a database.',
        'url': 'https://cristianarboleda.onrender.com',
        'img': 'link_in_bio_cristian',
        'tools': ['python', 'css', 'html', 'dash', 'postgresql'],
    }
]

def create_project(index=0):
    return html.A(
        href=project_data[index]['url'],
        className='carousel_project_element',
        target='_blank',
        children=[
            html.P(
                project_data[index]['title'].replace('_', ' ').title(),
                className='carousel_title',
            ),
            html.Img(
                src=url_img + project_data[index]['img'] + '.png',
                className='carousel_project_img',
            ),
            html.P(project_data[index]['description'])
        ],
    )

project_grid = html.Div(
    id='project_grid_container',
    children=[
        html.A(
            className='project_grid_element',
            children=[
                html.P(
                    project['title'],
                    style={'grid-row': '1'}
                ),
                html.Img(
                    src = url_img + project['img'] + '.png',
                    className='project_grid_img',
                    style={'grid-row': '2'}
                ),
                html.P(
                    project['description'],
                    style={'grid-row': '3'}
                ),
                html.P(
                    'tools',
                    style={'grid-row': '4'}
                )
            ]
        )
        for project in project_data
    ]
)

layout = html.Div(
    id='project_container',
    children=[
        html.Div(
            className='carousel_project_container',
            children=[
                html.Button('⟨', id='prev_btn', className='btn_carousel'),
                html.Div(id='carousel_project_container', children=create_project()),
                html.Button('⟩', id='next_btn', className='btn_carousel'),
                dcc.Store(id='current_index', data=0)
            ]
        ),
        project_grid,
    ]
)

@callback(
    Output('current_index', 'data'),
    Output('carousel_project_container', 'children'),
    Input('next_btn', 'n_clicks'),
    Input('prev_btn', 'n_clicks'),
    Input('current_index', 'data'),
    prevent_initial_call=True,
)
def update_carousel(next_btn, prev_btn, current_index):
    
    trigger = ctx.triggered_id
    total_projects = len(project_data)
    print('total_projects', total_projects)
    
    if trigger == 'next_btn':
        current_index += 1
        if current_index > (total_projects - 1):
            current_index = 0
    
    elif trigger == 'prev_btn':
        current_index -= 1
        if current_index < -total_projects:
            current_index = -1
    
    print(current_index)
    return current_index, create_project(current_index)