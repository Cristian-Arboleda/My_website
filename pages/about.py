from dash import register_page, html
import dash_leaflet as dl

register_page(__name__, path='/')

# -------------------------------------------------------------------------------------------------------------------

title = "Hello. I'm Cristian"
text = '''
I am a self-taught enthusiast with a strong academic foundation in statistics, programming, and artificial intelligence. 
I continuously update that foundation through targeted courses and hands-on practice. 
Responsible, punctual, and highly committed, I deliver data-driven analysis and well-structured, production-ready code. 
I’m results-oriented, detail-focused, and always eager to learn new tools. 
I’m looking for opportunities to contribute rigorous analysis, scalable solutions, and measurable impact to challenging projects.
'''

presentation = html.Div(
    id='container_presentation',
    children=[
        html.Div(
            id='presentation_text',
            children=[
                html.P(children=title, id='title_presentation'),
                html.P(children=text, id='body_presentation'),
            ]
        ),
        html.Img( src='assets/images/profile.png', id='img_profile'),
    ]
)

# -------------------------------------------------------------------------------------------------------------------

center = (4.5709, -74.2973)
map = html.Div(
    className='content_element',
    style={'grid-column': ' span 7', 'grid-row': 'span 8', 'flex-direction': 'column'},
    children=[
        dl.Map(
            center=center,
            zoom=4.5,
            className='img_content',
            children=[
                dl.TileLayer(),
                dl.Marker(
                    position=(4.7110, -74.0721),
                    children=dl.Tooltip("Bogotá")
                )
            ]
        ),
        html.P(
            children="Soy de Colombia, un país extraordinario, lleno de paisajes impresionantes y maravillas naturales que inspiran admiración."
        )
    ]
)

map_2 = html.Div(
    className='content_element',
    style={'grid-row': '9 / span 8', 'grid-column': '11 / span 8'},
    children=[
        html.Iframe(
            src="/assets/cesium_map.html",
            className='img_content'
        )
    ]
)
# -------------------------------------------------------------------------------------------------------------------

texto = '''
Aunque no pude continuar mis estudios por motivos de tiempo y recursos económicos, 
esa experiencia fue fundamental para desarrollar las bases que sigo fortaleciendo de manera autodidacta.
'''
img_uni = 'assets/images/uni.png'
university = html.Div(
    className='content_element',
    style={'grid-column': ' span 6', 'grid-row': ' span 3', 'flex-direction': 'row'},
    children=[
        html.Div(
            className='',
            children=[
                html.P(
                    """
                    Estudié seis semestres en la Universidad del Valle, donde adquirí una sólida base académica en mi campo.
                    """
                )
            ]
        ),
        html.Img(src=img_uni, className='img_content')
    ]
)

img_dinosaur = 'assets/images/dinosaur.gif'
dinosaurs = html.Div(
    style={'grid-column': 'span 6', 'grid-row': 'span 6', 'flex-direction': 'column',},
    className='content_element',
    children=[
    html.Img(src=img_dinosaur, className='img_content', style={'height': '80%'}),
    html.P(
        'Los humanos modernos hemos estado en la Tierra durante aproximadamente el 0.18% del tiempo que existieron los dinosaurios.',
        className='text_content',
    )
    ]
)

img_carl_sagan = 'assets/images/carl_sagan.jpg'
carl_sagan = html.Div(
    className='content_element',
    style={'grid-column': '5', 'grid-row': '3 / span 2', 'flex-direction': 'column'},
    children=[
        html.Img(src=img_carl_sagan, className='img_content'),
        html.P(children='Carl Sagan fue una figura clave en mi infancia, pues gracias a él descubrí mi interés por la ciencia y el conocimiento.')
    ]
)

black_hole = html.Div(
    className='content_element',
    #style={'grid-column': '3 / span 2', 'grid-row': '2 / span 2', 'flex-direction': 'column'},
    children=[
        html.Img(
            src='assets/images/black_hole.gif',
            className='img_content',
        ),
        html.P(
            children='''“Somos el modo que tiene el cosmos de conocerse a sí mismo.”'''
        ),
        html.P('“La imaginación a menudo nos lleva a mundos que nunca existieron, pero sin ella no vamos a ninguna parte.”'),
        html.P('- Carl Sagan')
    ]
)

text = """
Me gustan los gatos, aunque eso no significa que no me agraden los perros. 
En realidad, ambos me gustan, pero siento una atracción especial por los gatos.
"""
cat = html.Div(
    className='content_element',
    style={'grid-column': '  span 6', 'grid-row': '  span 4', 'display': 'flex', 'flex-direction': 'row'},
    children=[
        html.Img(src='assets/images/cat.png', className='img_content'),
        html.P(children=text)
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
        html.Img(src='assets/images/data.gif', className='img_content', style={'width': '200px', 'height': '150px'}),
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
            src='assets/images/data_8.gif', 
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
        html.Img(src='assets/images/idea.gif', className='img_content'),
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
        html.Img(src='assets/images/data_5.gif', className='img_content',),
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
        html.Img(src='assets/images/data_6.gif', className='img_content', style={'width': '200px', 'height': '200px'}),
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
                html.Img(src='assets/images/data_7.gif', className='img_content')
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
        #cat,
        #carl_sagan,
        #dinosaurs,
        #black_hole,
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

layout = html.Div(
    id='container_about',
    children=[
        html.Link(rel='stylesheet', href='assets/css/about.css'),
        presentation,
        content,
    ]
)