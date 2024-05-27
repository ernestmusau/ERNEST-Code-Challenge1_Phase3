class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def add_article(self, magazine, title):
        from models import Article  # Import Article here to avoid circular import issues
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    @property
    def articles(self):
        return self._articles

    @property
    def topic_areas(self):
        return {article.magazine.category for article in self._articles}
