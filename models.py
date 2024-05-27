class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    @property
    def articles(self):
        return self._articles

    @property
    def topic_areas(self):
        return {article.magazine.category for article in self._articles}


class Magazine:
    _all = []

    def __init__(self, name, category):
        if len(name) < 3:
            raise ValueError("Magazine name must be at least 3 characters long")
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all.append(self)

    def add_article(self, article):
        self._articles.append(article)

    @property
    def articles(self):
        return self._articles

    @property
    def contributors(self):
        return {article.author for article in self._articles}

    @property
    def article_titles(self):
        return [article.title for article in self._articles]

    @classmethod
    def top_publisher(cls):
        author_count = {}
        for magazine in cls._all:
            for article in magazine.articles:
                if article.author not in author_count:
                    author_count[article.author] = 0
                author_count[article.author] += 1

        top_author = max(author_count, key=author_count.get)
        for magazine in cls._all:
            if top_author in {article.author for article in magazine.articles}:
                return magazine


class Article:
    def __init__(self, author, magazine, title):
        if len(title) < 3:
            raise ValueError("Article title must be at least 3 characters long")
        self._author = author
        self._magazine = magazine
        self._title = title
        magazine.add_article(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title
