from flask import render_template, request,redirect,url_for
from . import main
from ..requests import get_highlights, search_news, get_sources

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    message = 'Welcome to News Highlight App'
    title = 'News Highlight'

    # Getting news highlight
    business_highlights = get_highlights('business')
    sports_highlights = get_highlights('sports')
    weather_highlights = get_highlights('weather')
    tech_highlights = get_highlights('tech')
    politics_highlights = get_highlights('politics')
    news_sources = get_sources()

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('.search', news_name = search_news))
    else:
        return render_template('index.html', text = message, title = title, business = business_highlights, source = news_sources,sports = sports_highlights, weather = weather_highlights, tech = tech_highlights, politics = politics_highlights)

@main.route('/article/<id>')

def NewsHighlight(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title, article = article)

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''

    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html', news = searched_news)    

    