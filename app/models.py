class NewsHighlight:
    '''
    NewsHightlight class to define highlight Objects
    '''

    def __init__(self, id, source, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.source = source
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Source:
    '''highlight
    Source class to define source objects
    '''

    def __init__(self,id,name,description,url,language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url =url
        self.language = language
        self.country = country 
        

