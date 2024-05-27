from models import Author, Magazine, Article

def main():
    author = Author("Gloria Mumbe")
    magazine = Magazine("Tech Weekly", "Technology")
    article = author.add_article(magazine, "The Future of AI")

    print(f"Author: {author.name}")
    print(f"Magazine: {magazine.name}")
    print(f"Article: {article.title}")
    print(f"Articles by Author: {[article.title for article in author.articles]}")
    print(f"Articles in Magazine: {[article.title for article in magazine.articles]}")

if __name__ == "__main__":
    main()