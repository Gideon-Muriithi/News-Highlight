from app import app
import urllib.request,json
from .models import news_highlight

NewsHighlight = news_highlight.NewsHighlight

#Getting api key
api_key = app.config['NEWS_HIGHLIGHT_API_KEY']

# Getting the news highlight base url
base_url = app.config["ARTICLES_API_BASE_URL"]


def get_highlights(category):
    '''We then use with as our context manager to send a request using theurllib.request.urlopen() function that takes in the get_movies_url as an argument and sends a request as url

    Function that gets the json response to our url request
    '''
    get_highlights_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_highlights_url) as url:
        get_highlights_data = url.read()
        get_highlights_response = json.loads(get_highlights_data)

        highlight_results = None

        if get_highlights_response['articles']:
            highlight_results_list = get_highlights_response['articles']
            highlight_results = process_results(highlight_results_list)


    return highlight_results

def process_results(highlight_list):
    '''
    Function  that processes the news highlights result and transform them to a list of Objects

    Args:
        highlight_list: A list of dictionaries that contain highlight details

    Returns :
        highlight_results: A list of highlight objects
    '''
    highlight_results = []

    for highlight_item in highlight_list:
        id = highlight_item.get("source['id']")
        source = highlight_item.get('source.name')
        title = highlight_item.get('title')
        description = highlight_item.get('description')
        url = highlight_item.get('url')
        urlToImage = highlight_item.get('urlToImage')
        publishedAt = highlight_item.get('publishedAt')

        if urlToImage:
            highlight_object = NewsHighlight(id, source, title, description, url, urlToImage, publishedAt)
            highlight_results.append(highlight_object)

    return highlight_results

def get_sources():

    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        url_object = None
        if article_details_response:
            id = article_details_response.get('id')
            source = article_details_response.get('source.name')
            title = article_details_response.get('title')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            urlToImage = article_details_response.get('urlToImage')
            publishedAt = article_details_response.get('publishedAt')

            url_object = NewsHighlight(id, source, title, description, url, urlToImage, publishedAt)

    return url_object

def search_news(news_name):

    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(api_key, news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results