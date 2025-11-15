from dash import register_page, html

register_page(__name__, path='/')

# -------------------------------------------------------------------------------------------------------------------
presentation = html.Div(
    id='container_presentation',
    children=[
        html.Div(
            id='presentation_text',
            children=[
                html.P(children="Hello! My name is Cristian.", id='title_presentation'),
                html.Div(
                    className='body_presentation',
                    children=[
                        html.P("I am a data analysis professional with a background in statistics and hands-on experience in Python. I design and develop interactive dashboards using Dash, automate repetitive tasks with Selenium, and perform web scraping to collect relevant data.",),
                        html.P("From this information, I carry out rigorous analyses in Python to transform raw data into actionable insights that support decision-making. In addition, I apply machine learning techniques to develop predictive and classification models, validate their performance, and uncover patterns that enhance automated solutions."),
                        html.P("I am constantly updating my skills and enjoy tackling real-world problems with evidence-based solutions.")
                    ]
                )
            ]
        ),
        html.Img( src='assets/images/about/profile.png', id='img_profile'),
    ]
)

# -------------------------------------------------------------------------------------------------------------------

map_2 = html.Div(
    className='content_element',
    style={'grid-row': '9 / span 10', 'grid-column': '11 / span 8', 'flex-direction': 'column'},
    children=[
        html.Iframe(
            src="/assets/cesium_map.html",
            className='img_content', style={'border': 'none'}
        ),
        html.P(
            [
                'I’m from Colombia — an extraordinary country filled with stunning landscapes and natural wonders that inspire admiration.'
            ],
            
        ),
        html.Span('(Double-click on the map)')
    ]
)

# -------------------------------------------------------------------------------------------------------------------
university = html.Div(
    className='content_element',
    style={'grid-column': '6 / span 5', 'grid-row': '23 / span 5', 'flex-direction': 'row'},
    children=[
        html.Div(
            className='',
            children=[
                html.P('I studied six semesters of Statistics at the Universidad del Valle, where I acquired a solid academic foundation in my field.')
            ]
        ),
        html.Img(src='assets/images/about/uni.png', className='img_content', style={'width': '140px', 'height': '220px'})
    ]
)

dinosaurs = html.Div(
    style={'grid-column': '11 / span 7', 'grid-row': '19 / span 8', 'flex-direction': 'column',},
    className='content_element',
    children=[
        html.Img(src='assets/images/about/dinosaur.gif', className='img_content', style={'height': '350px'}),
        html.P([
            'Modern humans have been on Earth for ',
            html.Span('approximately 0.18% of the time '),
            'that the dinosaurs existed.'
        ])
    ]
)

img_carl_sagan = 'assets/images/about/carl_sagan.jpg'
carl_sagan = html.Div(
    className='content_element',
    style={'grid-column': '7 / span 4', 'grid-row': '17 / span 7', 'flex-direction': 'column'},
    children=[
        html.Img(src=img_carl_sagan, className='img_content'),
        html.P(children='Carl Sagan fue una figura clave en mi infancia, pues gracias a él descubrí mi interés por la ciencia y el conocimiento.')
    ]
)

black_hole = html.Div(
    className='content_element',
    style={'grid-column': '2 / span 9', 'grid-row': '17 / span 6', 'flex-direction': 'column'},
    children=[
        html.Img(
            src='assets/images/about/black_hole.gif',
            className='img_content',
        ),
        html.P(children='“We are a way for the cosmos to know itself.”',),
        html.P('- Carl Sagan', )
    ]
)

cat = html.Div(
    className='content_element',
    style={'grid-column': '1 / span 5', 'grid-row': '23 / span 5', 'display': 'flex', 'flex-direction': 'row'},
    children=[
        html.Img(src='assets/images/about/cat.png', className='img_content', style={'width': '150px', 'height': '240px'}),
        html.P(children='I like both cats and dogs, although I feel a special attraction to cats.')
    ]
)

data = html.Div(
    className='content_element',
    style={'grid-row': '1 / span 4', 'grid-column': '1 / span 8'},
    children=[
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P(
                    children ="""
                    Nowadays, we generate more information in a single year than in all of previous human history.
                    """, 
                ),
                html.P(
                    children ="""
                    Every second, millions of data points are produced through social networks, digital transactions, connected devices, and online services.
                    """, 
                ),
            ]
        ),
        html.Img(src='assets/images/about/data.gif', className='img_content', style={'width': '200px', 'height': '150px'}),
    ]
)

data_9 = html.Div(
    className='content_element',
    style={'grid-row': '1 / span 4', 'grid-column': '9 / 4 span'},
    children=[
        html.P([
            "According to recent estimates, the world generates more than  ",
            html.Span('300 exabytes '),
            'of data per day, and this figure continues to grow exponentially.',
        ]),
    ]
)

data_2 = html.Div(
    className='content_element',
    style={
        'flex-direction': 'column', 'grid-row': '1 / span 4', 'grid-column': '13 / span 6',
        'position': 'relative', 'overflow': 'visible'
        },
    children=[
        html.Img(
            src='assets/images/about/data_8.gif', 
            className='img_content',
            style={
                'position': 'absolute', 'top': '-190px', 'height': '300px', 'width': '300px'
            }
        ),
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column',},
            children=[
                html.P([ 
                    """
                    However, data has no value in itself; it must be analyzed, interpreted, and 
                    """,
                    html.Span(' transformed into useful information.')
                    ]
                ),
            ]
        ),
    ]
)

data_4 = html.Div(
    className='content_element',
    style={'grid-row': '5 / span 4', 'grid-column': '1 / span 9'},
    children=[
        html.Img(src='assets/images/about/idea.gif', className='img_content'),
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P([
                    """
                    It’s astonishing how powerful data can be in answering questions: 
                    it allows us to understand ourselves and the reality around us with greater precision, and on that basis, 
                    """,
                    html.Span('make truly informed decisions.')
                ]),
            ]
        ),
    ]
)

data_5 = html.Div(
    className='content_element',
    style={'grid-row': '5 / span 4', 'grid-column': '10 / span 9'},
    children=[
        html.Img(src='assets/images/about/data_5.gif', className='img_content',),
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P(
                    """
                    The ability to program allows us to transform an idea into a tangible project; 
                    each line of code is a brushstroke that brings something new, functional, and creative to life.
                    """
                ),
                html.Span('It’s like turning logic into art.')
            ]
        )
    ]
)


data_7 = html.Div(
    className='content_element',
    style={'grid-row': '9 / span 8', 'grid-column': '6 / span 5', 'flex-direction': 'column'},
    children=[
        html.Img(src='assets/images/about/data_6.gif', className='img_content', style={'width': '200px', 'height': '200px'}),
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P([
                    """
                    I have participated in several team projects, although I developed most of them on my own. 
                    That experience allowed me to strengthen my knowledge and learn through hands-on practice.
                    """,
                ]),
                html.Span('I am always seeking to stay up to date and eager to keep learning.')
            ]
        ),
    ]
)

data_8 = html.Div(
    className='content_element',
    style={'grid-row': '9 / span 3', 'grid-column': '1 / span 5',},
    children=[
        html.Div(
            className='text_container_content',
            children=[
                html.P([
                    """
                    In the digital era, data, statistics, and artificial intelligence are strategic assets for any company: 
                    data reveal behaviors and allow results to be measured.
                    """,
                ]),
            ],
        ),
    ]
)

data_10 = html.Div(
    className='content_element',
    style={'grid-row': '12 / span 5', 'grid-column': '1 / span 5', 'text-align': 'start'},
    children=[
        html.Div(
            className='text_container_content',
            children=[
                html.Img(src='assets/images/about/data_7.gif', className='img_content')
            ]
        ),
    ]
)

# -------------------------------------------------------------------------------------------------------------------
content = html.Div(
    id='container_content',
    children=[
        map_2,
        university, 
        cat,
        #carl_sagan,
        dinosaurs,
        black_hole,
        data,
        data_2,
        data_4,
        data_5,
        data_7,
        data_8,
        data_9,
        data_10,
    ]
)
# -------------------------------------------------------------------------------------------------------------------
spaceship = html.Div(
    className='spaceship_container',
    children=[
        html.Img(src='assets/images/about/spaceship.gif', className='spaceship')
    ]
)


# -------------------------------------------------------------------------------------------------------------------

layout = html.Div(
    id='container_about',
    children=[
        html.Link(rel='stylesheet', href='assets/css/about.css'),
        presentation,
        content,
        spaceship,
    ]
)