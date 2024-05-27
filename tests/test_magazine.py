import pytest # type: ignore
from author import Author
from magazine import Magazine

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

