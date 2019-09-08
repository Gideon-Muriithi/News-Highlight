from flask import render_template
from app import app
from .requests import get_highlights, get_article

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

@app.route('/article/id')

def NewsHighlight(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title, article = article)