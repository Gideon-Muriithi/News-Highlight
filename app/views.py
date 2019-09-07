from flask import render_template
from app import app
from .requests import get_highlights

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    message = 'Welcome to News Highlight App'
    title = 'News Highlight'

    # Getting popular highlight
    business_highlights = get_highlights('business')
    sports_highlights = get_highlights('sports')
    weather_highlights = get_highlights('weather')
    tech_highlights = get_highlights('tech')
    politics_highlights = get_highlights('politics')

    # print(popular_highlights)

    return render_template('index.html', text = message, title = title, business = business_highlights,
    sports = sports_highlights, weather = weather_highlights, tech = tech_highlights, politics = politics_highlights)