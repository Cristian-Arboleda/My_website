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
    style={'grid-column': 'span 2', 'grid-row': 'span 2',},
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
Estudié seis semestres en la Universidad del Valle, donde adquirí una sólida base académica en mi campo. 
Aunque no pude continuar mis estudios por motivos de tiempo y recursos económicos, 
esa experiencia fue fundamental para desarrollar las bases que sigo fortaleciendo de manera autodidacta.
'''
img_uni = 'assets/images/uni.png'
university = html.Div(
    className='content_element',
    style={'grid-column': 'span 2', 'grid-row': 'span 1', 'flex-direction': 'row'},
    children=[
        html.P(children=texto,),
        html.Img(src=img_uni, className='img_content')
    ]
)

img_dinosaur = 'assets/images/dinosaur.gif'
text_dinosaurs = """

"""
dinosaurs = html.Div(
    style={'grid-column': 'span 2', 'grid-row': 'span 2'},
    className='content_element',
    children=[
    html.Img(src=img_dinosaur, className='img_content')
    ]
)

img_carl_sagan = 'assets/images/carl_sagan.jpg'
carl_sagan = html.Div(
    className='content_element',
    style={'grid-column': '5', 'grid-row': '1 / span 2'},
    children=[
        html.Img(src=img_carl_sagan, className='img_content')
    ]
)

video_black_hole = 'assets/images/black_hole_2.mp4'
black_hole = html.Div(
    className='content_element',
    style={'grid-column': 'span 2', 'grid-row': 'span 2'},
    children=[
        html.Video(
            src=video_black_hole,
            className='img_content',
            autoPlay=True,
            loop=True,
            muted=True,
            controls=False,
        )
    ]
)

text = """
Me gustan los gatos, aunque eso no significa que no me agraden los perros. 
En realidad, ambos me gustan, pero siento una atracción especial por los gatos.
"""
cat = html.Div(
    className='content_element',
    style={'grid-column': 'span 2', 'grid-row': 'span 1', 'display': 'flex', 'flex-direction': 'row'},
    children=[
        html.Img(src='assets/images/cat.png', className='img_content'),
        html.P(children=text)
    ]
)
# -------------------------------------------------------------------------------------------------------------------
content = html.Div(
    id='container_content',
    children=[
        map,
        university,
        cat,
        carl_sagan,
        dinosaurs,
        black_hole,
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