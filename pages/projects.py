from dash import register_page, html

register_page(__name__)

data = [
    {
        'title': 'twitch_notificacion_bot', 
        'description': 'A Discord bot developed in Python whose purpose is to automatically notify when a Twitch channel goes live.', 
        'url': 'https://github.com/Cristian-Arboleda/bot_biscuittp_twitch_avisos', 
        'image': 'twitch_notificacion_bot',
        'tools': ['python']
    },
    {
        'title': 'link_in_bio_biscuittp',
        'description': 'A page that displays a brief description about me and gathers all the links to my personal social media profiles.',
        'url': 'https://biscuittp-stream.onrender.com',
        'image': 'link_in_bio_biscuittp',
        'tools': ['python', 'css', 'html', 'dash']
    },
    {
        'title': 'welcome_bot_for_discord',
        'description': 'A Discord bot that welcomes new server members by mentioning their name and displaying a personalized image.',
        'url': 'https://github.com/Cristian-Arboleda/bot-bienvenida',
        'tools': ['python']
    },
    {
        
    }
]


layout = html.Div()