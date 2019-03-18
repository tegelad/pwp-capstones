""" Main Tomerater Codeacademy File """

import re

class User:
    """User object class for Tomerater"""
    def __init__(self, name, email):
        if isinstance(name, str) and isinstance(email, str):
            self.name = name
            self.email = email
            self.books = {}

    def get_email(self):
        """Function to return user's email address"""
        return self.email

    def change_email(self, address):
        """Function to change user's email address"""
        if isinstance(address, str):
            self.email = address
            string = '{name} has been changed from {oldAddr} to {newAddr}'
            print(string.format(name=self.name, oldAddr=self.email, newAddr=address))

    def read_book(self, book, rating=None):
        """Function to add book to users rating list"""
        self.books[book] = rating

    def get_average_rating(self):
        """Function to get average ratings of users books"""
        val = 0
        for rating in self.books.values():
            if rating is None:
                val += 0
            else:
                val += rating
        return val / len(self.books)

    def __repr__(self):
        return 'User {user}, email: {email}, books read: {bookNum}'.format(
            user=self.name, email=self.email, bookNum=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

class Book:
    """Book object class for Tomerater"""
    def __init__(self, title, isbn, price=None):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def get_title(self):
        """Function to get Book Title"""
        return self.title

    def get_isbn(self):
        """Function to get Book ISBN"""
        return self.isbn

    def set_isbn(self, new_isbn):
        """Function to set Book ISBN"""
        print("{book} ISBN has been updated to {isbn}".format(book=self.title, isbn=new_isbn))
        self.isbn = new_isbn

    def add_rating(self, rating):
        """Function to add Book rating"""
        if isinstance(rating, int):
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid rating {}, please enter a number between 0 and 4".format(rating))

    def get_average_rating(self):
        """ Function to get average book ratings"""
        #val = 0
        #for rating in self.ratings:
        #    val += rating
        #return val / len(self.ratings)
        return sum([rating for rating in self.ratings]) / len(self.ratings)

    def __eq__(self, otherBook):
        return self.title == otherBook.title and self.isbn == otherBook.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return '{title} with ISBN {isbn} and price of {price}'.format(
            title=self.title, isbn=self.isbn, price=self.price)

class Fiction(Book):
    """Fiction subclass of Book Class for Tomerater"""
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        """Get Author Function for Fiction Subclass"""
        return self.author

    def __repr__(self):
        return '{title} by {author}'.format(title=self.title, author=self.author)

class NonFiction(Book):
    """Non-Fiction subclass of Book Class for Tomerater"""
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        """Get Subject Function for Non-Fiction Book Object"""
        return self.subject

    def get_level(self):
        """Get Reading Level Function for Non-Fiction Book Object"""
        return self.level

    def __repr__(self):
        return '{title}, a {level} manual on {subject}'.format(
            title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    """ Main Class For Codeacademy Project"""
    def __init__(self):
        self.users = {}
        self.books = {}

    @classmethod
    def create_book(cls, title, isbn, price=None):
        """Create Book entry Object for main class"""
        return Book(title, isbn, price)

    @classmethod
    def create_novel(cls, title, author, isbn, price=None):
        """Create Novel entry Object for main class"""
        return Fiction(title, author, isbn, price)

    @classmethod
    def create_non_fiction(cls, title, subject, level, isbn, price=None):
        """Create Non-Fiction entry Object for main class"""
        return NonFiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        """Add book to user Function for main class"""
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No User with email {email}".format(email=email))

    def add_user(self, name, email, user_books=None):
        """Add user Function for Main Class"""
        email_search = re.search(".*@.*.(com|edu|org)", email, re.M|re.I)
        if email not in self.users:
            if email_search:
                self.users[email] = User(name, email)
                if user_books is not None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
            else:
                print("email address {} is not valid".format(email))
        else:
            print("User {} already exists".format(email))

    def print_catalog(self):
        """Print All Books Function"""
        return '\n'.join([str(book) for book in self.books])

    def print_users(self):
        """Print All Users Function"""
        return '\n'.join([str(user.name) for user in self.users.values()])

    def most_read_book(self):
        """Find most read book function"""
        most_read = ''
        highest_read = float('-inf')
        for book in self.books:
            if self.books[book] > highest_read:
                highest_read = self.books[book]
                most_read = book
        return most_read

    def highest_rated_book(self):
        """Find highest rated book funciton"""
        highest_rated_book = ''
        max_book_rating = float('-inf')

        for book in self.books:
            if book.get_average_rating() > max_book_rating:
                max_book_rating = book.get_average_rating()
                highest_rated_book = book

        return highest_rated_book

    def most_positive_user(self):
        """Find most positive reviewer function"""
        positive_user = ''
        max_positive_avg = float('-inf')

        for user in self.users.values():
            if user.get_average_rating() > max_positive_avg:
                max_positive_avg = user.get_average_rating()
                positive_user = user.name

        return positive_user

    def __repr__(self):
        return 'Object has {users} users and {books} books'.format(
            users=len(self.users), books=len(self.books))

    @classmethod
    def dict_val(cls, dict_info):
        """Function to return dictionary key's value"""
        return dict_info[1]

    def get_n_most_read_books(self, num_books):
        """Take N number and return N number of books that have been read (descending)"""
        return '\n'.join(
            [str(key[0]) for key in sorted(
                self.books.items(),
                key=self.dict_val, reverse=True
                )[:num_books]])

    def get_n_most_prolific_readers(self, num_books):
        """Take N number and return N users that have read the most books in descending order"""
        return '\n'.join(
            [
                str(key[0]) for key in sorted(
                    (
                        (
                            self.users[user].name,
                            len(self.users[user].books)
                            )
                        for user in self.users
                        ),
                    key=lambda tup: tup[1], reverse=True
                    )[:num_books]
                ]
            )

    def get_n_most_expensive_books(self, num_books):
        """Return N books with the highest price, add price variable for each book"""
        return '\n'.join(
            [
                str(key[0]) for key in sorted(
                    (
                        (
                            key.title,
                            key.price
                            )
                        for key in self.books
                        ),
                    key=lambda tup: tup[1], reverse=True
                    )[:num_books]
                ]
            )

    def get_worth_of_user(self, user_email):
        """Return the sum cost of all books read by the user"""
        return round(
            sum(
                [book.price for book in self.users[user_email].books]
                ), 2
            )
