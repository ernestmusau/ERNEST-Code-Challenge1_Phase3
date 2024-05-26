from author import Author
from magazine import Magazine
from article import Article

author1 = Author("John Doe")
author2 = Author("Jane Smith")

mag1 = Magazine("Tech Weekly", "Technology")
mag2 = Magazine("Health Today", "Health")

article1 = author1.add_article(mag1, "The Future of AI")
article2 = author1.add_article(mag2, "Healthy Living Tips")
article3 = author2.add_article(mag1, "Quantum Computing")

print(author1.articles())
print(author1.magazines())
print(mag1.articles())
print(mag1.contributors())
print(mag1.article_titles())
print(Magazine.top_publisher())
