import pytest # type: ignore
from author import Author
from magazine import Magazine

def test_author_initialization():
    author = Author("Gloria Mumbe")
    assert author.name == "Gloria Mumbe"

def test_author_invalid_name():
    with pytest.raises(ValueError):
        Author("")

def test_author_articles():
    author = Author("Gloria Mumbe")
    assert author.articles() == []

def test_author_add_article():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    article = author.add_article(magazine, "The Future of AI")
    assert article in author.articles()

def test_author_topic_areas():
    author = Author("Gloria Mumbe")
    magazine1 = Magazine("Tech Weekly", "Technology")
    magazine2 = Magazine("Health Today", "Health")
    author.add_article(magazine1, "The Future of AI")
    author.add_article(magazine2, "Healthy Living Tips")
    assert set(author.topic_areas()) == {"Technology", "Health"}
