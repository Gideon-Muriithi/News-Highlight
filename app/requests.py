import urllib.request,json
from .models import NewsHighlight, Source

#Getting api key
api_key = None

# Getting the article base url
base_url = None

# Getting the source base url
source_url = None


def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['ARTICLES_API_BASE_URL']
    source_url = app.config["NEWS_SOURCES_BASE_URL"]


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
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = source_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results

def process_sources(sources_list):
	'''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''
	sources_results = []

	for source_item in sources_list:
		id = source_item.get('id') 
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		language = source_item.get('language')
		country = source_item.get('country')


		sources_object = Source(id,name,description,url,country,language)
		sources_results.append(sources_object)


	return sources_results



def search_news(news_name):

    search_news_url = base_url.format(news_name, api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)
        
        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_results(search_news_list)


    return search_news_results