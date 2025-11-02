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
    style={'grid-column': 'span 2', 'grid-row': 'span 2', 'flex-direction': 'column'},
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
# -------------------------------------------------------------------------------------------------------------------

texto = '''
Aunque no pude continuar mis estudios por motivos de tiempo y recursos económicos, 
esa experiencia fue fundamental para desarrollar las bases que sigo fortaleciendo de manera autodidacta.
'''
img_uni = 'assets/images/uni.png'
university = html.Div(
    className='content_element',
    style={'grid-column': ' span 2', 'grid-row': ' span 1', 'flex-direction': 'row'},
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
    style={'grid-column': 'span 2', 'grid-row': 'span 2', 'flex-direction': 'column',},
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
    style={'grid-column': '  span 2', 'grid-row': '  span 1', 'display': 'flex', 'flex-direction': 'row'},
    children=[
        html.Img(src='assets/images/cat.png', className='img_content'),
        html.P(children=text)
    ]
)
programming = html.Div(
    className='content_element',
    style={'grid-row': '1 / span 2', 'grid-column': '5 / span 1'},
    children=[
        html.Video(
            src='assets/images/matrix.mp4',
            autoPlay=True,
            loop=True,
            controls=False,
            muted=True,
            className='img_content'
        ),
    ]
)

text = '''
En la actualidad, generamos más información en un solo año que en toda la historia previa de la humanidad. 
Cada segundo, millones de datos se producen a través de redes sociales, transacciones digitales, dispositivos conectados y servicios en línea. 
Según estimaciones recientes, el mundo genera más de 300 exabytes de datos al día, y esta cifra sigue creciendo exponencialmente.
'''
data = html.Div(
    className='content_element',
    style={'grid-row': '1 / span 1', 'grid-column': '3 / span 3'},
    children=[
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P(
                    children ="""
                    En la actualidad, generamos más información en un solo año que en toda la historia previa de la humanidad.
                    """, 
                ),
                html.P(
                    children ="""
                    Cada segundo, millones de datos se producen a través de redes sociales, transacciones digitales, dispositivos conectados y servicios en línea. 
                    """, 
                ),
                html.P([
                    "Según estimaciones recientes, el mundo genera más de ",
                    html.Span('300 exabytes '),
                    'de datos al día, y esta cifra sigue creciendo exponencialmente.',
                ]),
            ]
        ),
        html.Img(src='assets/images/data.gif', className='img_content', style={'width': '45%'}),
    ]
)

data_2 = html.Div(
    className='content_element',
    style={'flex-direction': 'column', 'grid-row': '2 / span 2', 'grid-column': '5 / span 1'},
    children=[
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column',},
            children=[
                html.P(
                    """
                    Estos datos, sin embargo, no tienen valor por sí solos: 
                    deben ser analizados, interpretados y transformados en conocimiento útil. 
                    """, 
                ),
                html.P(
                    """
                    La ciencia de datos, la inteligencia artificial y el análisis estadístico se han convertido en herramientas fundamentales para comprender patrones,
                    tomar decisiones informadas y crear innovaciones que impulsan el progreso en casi todos los campos del conocimiento.
                    """
                )
            ]
        ),
    ]
)

data_3 = html.Div(
    className='content_element',
    style={'grid-row': '3 / span 1', 'grid-column': '4 / span 1', 'flex-direction': 'column'},
    children=[
        html.Img(src='assets/images/idea.gif', className='img_content')
    ]
)

data_4 = html.Div(
    className='content_element',
    style={'grid-row': '3 / span 1', 'grid-column': '2 / span 2'},
    children=[
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P(
                    """
                    Es sorprendente la capacidad que tienen los datos para responder preguntas: 
                    nos permiten comprendernos a nosotros mismos y a la realidad que nos rodea con mayor precisión y, sobre esa base, 
                    tomar decisiones verdaderamente informadas.
                    """
                ),
                html.P(
                    """
                    Siempre que se apliquen procesos estadísticos adecuados, rigurosos y éticos.
                    """
                )
            ]
        ),
    ]
)


data_5 = html.Div(
    className='content_element',
    style={'grid-row': '2 / span 1', 'grid-column': '3 / span 2'},
    children=[
        html.Img(src='assets/images/data_5.gif', className='img_content',),
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P(
                    """
                    La habilidad de programar nos permite transformar una idea en un proyecto tangible; 
                    Cada línea de código es una pincelada que da vida a algo nuevo, funcional y creativo.
                    """
                ),
                html.Span('Es como convertir la lógica en arte.')
            ]
        )
    ]
)

data_6 = html.Div(
    style={'grid-row': '3 / span 1', 'grid-column': '1 / span 1'},
    className='content_element',
    children=[
        html.Img(
            className='img_content',
            src='assets/images/data_6.gif',
        )
    ],
)

data_7 = html.Div(
    className='content_element',
    style={'grid-row': '4 / span 1', 'grid-column': '1 / span 2'},
    children=[
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P([
                    'He participado en distintos proyectos en equipo, aunque la mayoría los desarrollé por mi cuenta. ',
                    'Eso me permitió afianzar mis conocimientos y aprender de forma práctica.',
                ]),
                html.P('Me mantengo siempre en constante actualización y con ganas de seguir aprendiendo.')
            ]
        )
    ]
)

data_8 = html.Div(
    className='content_element',
    style={'grid-row': '4 / span 1', 'grid-column': '3 / span 2'},
    children=[
        html.Div(
            className='text_container_content',
            style={'flex-direction': 'column'},
            children=[
                html.P([
                    'He participado en distintos proyectos en equipo, aunque la mayoría los desarrollé por mi cuenta. ',
                    'Eso me permitió afianzar mis conocimientos y aprender de forma práctica.',
                ]),
            ]
        ),
        html.Img(src='assets/images/data_7.gif')
    ]
)


# -------------------------------------------------------------------------------------------------------------------
content = html.Div(
    id='container_content',
    children=[
        map,
        university, 
        cat,
        #carl_sagan,
        #programming,
        dinosaurs,
        #black_hole,
        data,
        data_2,
        data_3,
        data_4,
        data_5,
        data_6,
        data_7,
        data_8,
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