class NewsHighlight:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self, id, source, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.source = source
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    