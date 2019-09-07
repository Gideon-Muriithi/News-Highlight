from app import app
import urllib.request,json
from .models import news_highlight

NewsHighlight = movie.NewsHighlight

#Getting api key
api_key = app.config['NEWS_HIGHLIGHT_API_KEY']

# Getting the new highlight base url
base_url = app.config["ARTICLES_API_BASE_URL"]


def get_highlights(category):
    '''We then use with as our context manager to send a request using theurllib.request.urlopen() function that takes in the get_movies_url as an argument and sends a request as url


    Function that gets the json response to our url request
    '''
    get_highlights_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_highlights_url) as url:
        get__highlights_data = url.read()
        get_highlights_response = json.loads(get_highlights_data)

        highlight_results = None

        if get_highlights_response['results']:
            highlight_results_list = get_highlights_response['results']
            highlight_results = process_results(highlight_results_list)


    return highlight_results