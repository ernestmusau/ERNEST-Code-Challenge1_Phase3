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
