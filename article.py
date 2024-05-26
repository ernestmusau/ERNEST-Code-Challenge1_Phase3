class Article:
    def __init__(self, author, magazine, title):
        from author import Author
        from magazine import Magazine

        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        if len(title) < 5:
            raise ValueError("title must be at least 5 characters long")

        self.author = author
        self.magazine = magazine
        self.title = title
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
