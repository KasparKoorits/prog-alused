"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        for ibook in self.books:
            if ibook.title == book.title:
                return False

        if book not in self.books and book.rating >= self.rating:
            return True
        else:
            return False

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        if book in self.books:
            return True
        else:
            return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        bookl = []
        for bookp in self.books:
            bookl.append(bookp)
        books_sorted = sorted(bookl, key=lambda bookl: bookl.price, reverse=False)
        return books_sorted

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        highestrating = 0
        bestbooks = []
        for bestrating in self.books:
            if bestrating.rating > highestrating:
                highestrating = bestrating.rating
        for bestrating in self.books:
            if bestrating.rating == highestrating:
                bestbooks.append(bestrating)
        return bestbooks
