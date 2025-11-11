from dash import register_page, html, dcc, callback, Input, Output, State, no_update, ctx

register_page(__name__)

url_img = 'assets/images/project/'
url_tools = 'assets/images/tools/'

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

# ----------------------------------------------------------------------------------------------------------------------------------
def create_project(index=0):
    return html.A(
        href=project_data[index]['url'],
        className='project_carousel_element',
        target='_blank',
        children=[
            html.P(
                project_data[index]['title'].replace('_', ' ').title(),
                className='carousel_title',
            ),
            html.Img(
                src=url_img + project_data[index]['img'] + '.png',
                className='project_carousel_img',
            ),
            html.P(
                project_data[index]['description'],
                className='carousel_description'
            ),
            html.Div(
                className='carousel_tools',
                children=[
                    html.Img(
                        src=url_tools + tool + '.png',
                        className='carousel_tool_img'
                    )
                    for tool in project_data[index]['tools']
                ]
            )
        ],
    )

project_carousel = html.Div(
    className='project_carousel_container',
    children=[
        html.Div(id='project_carousel_container', children=create_project()),
        dcc.Store(id='current_index', data=0),
        html.Div(
            className='carousel_btn_container',
            children=[
                html.Button('⟨', id='prev_btn', className='carousel_btn'),
                html.Button('⟩', id='next_btn', className='carousel_btn'),
            ]
        )
    ]
)

# ----------------------------------------------------------------------------------------------------------------------------------

project_grid = html.Div(
    id='project_grid_container',
    children=[
        html.A(
            href=project['url'],
            className='project_grid_element',
            children=[
                html.P(
                    project['title'].replace('_', ' ').title(),
                    style={'grid-row': '1'},
                    className='project_grid_title'
                ),
                html.Img(
                    src = url_img + project['img'] + '.png',
                    className='project_grid_img',
                    style={'grid-row': '2'}
                ),
                html.P(
                    project['description'],
                    style={'grid-row': '3'},
                    className='project_grid_description'
                ),
                html.Div(
                    className='project_grid_tools_container',
                    style={'grid-row': '4'},
                    children=[
                        html.Img(
                            src=url_tools + tool + '.png',
                            className='project_grid_tool_img'
                        )
                        for tool in project['tools']
                    ]
                ),
            ]
        )
        for project in project_data
    ]
)

# ----------------------------------------------------------------------------------------------------------------------------------
layout = html.Div(
    id='project_container',
    children=[
        project_carousel,
        html.Hr(style={'color': 'white', 'width': '100%'}),
        project_grid,
    ]
)

@callback(
    Output('current_index', 'data'),
    Output('project_carousel_container', 'children'),
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