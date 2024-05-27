import pytest # type: ignore

class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    
def test_author_add_article():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    article = author.add_article(magazine, "The Future of AI")
    assert article in author.articles()

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

class Magazine:
    def __init__(self, name, category):
        if not category:
            raise ValueError("Category must not be empty")
        self.name = name
        self.category = category
        self._articles = []

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return {article.author for article in self._articles}

    def article_titles(self):
        return [article.title for article in self._articles]

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

def test_magazine_invalid_category():
    with pytest.raises(ValueError):
        Magazine("Tech Weekly", "")

def test_magazine_articles():
    magazine = Magazine("Tech Weekly", "Technology")
    assert magazine.articles() == []

def test_magazine_contributors():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    article = author.add_article(magazine, "The Future of AI")
    assert author in magazine.contributors()

def test_magazine_article_titles():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    article = author.add_article(magazine, "The Future of AI")
    assert magazine.article_titles() == ["The Future of AI"]

test_magazine_invalid_category()
test_magazine_articles()
test_magazine_contributors()
test_magazine_article_titles()

