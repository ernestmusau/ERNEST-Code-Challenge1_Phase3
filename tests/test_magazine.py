import pytest # type: ignore
from magazine import Magazine
from author import Author

def test_magazine_initialization():
    magazine = Magazine("Tech Weekly", "Technology")
    assert magazine.name == "Tech Weekly"
    assert magazine.category == "Technology"

def test_magazine_invalid_name():
    with pytest.raises(ValueError):
        Magazine("T", "Technology")

def test_magazine_invalid_category():
    with pytest.raises(ValueError):
        Magazine("Tech Weekly", "")

def test_magazine_articles():
    magazine = Magazine("Tech Weekly", "Technology")
    assert magazine.articles() == []

def test_magazine_contributors():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    author.add_article(magazine, "The Future of AI")
    assert author in magazine.contributors()

def test_magazine_article_titles():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    author.add_article(magazine, "The Future of AI")
    assert magazine.article_titles() == ["The Future of AI"]

def test_magazine_top_publisher():
    magazine1 = Magazine("Tech Weekly", "Technology")
    magazine2 = Magazine("Health Today", "Health")
    author = Author("Gloria Mumbe")
    author.add_article(magazine1, "The Future of AI")
    author.add_article(magazine1, "AI and Society")
    author.add_article(magazine2, "Healthy Living Tips")
    assert Magazine.top_publisher() == magazine1
