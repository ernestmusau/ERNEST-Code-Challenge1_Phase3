import pytest # type: ignore
from article import Article
from author import Author
from magazine import Magazine

def test_article_initialization():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    article = Article(author, magazine, "The Future of AI")
    assert article.title == "The Future of AI"
    assert article.author == author
    assert article.magazine == magazine

def test_article_invalid_title():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    with pytest.raises(ValueError):
        Article(author, magazine, "AI")
