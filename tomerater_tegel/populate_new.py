""" Main population test script for CodeAcademy Project"""

import tome_rater

MYTR = tome_rater.TomeRater()

#Create some books:
BOOK_1 = MYTR.create_book("Society of Mind", 12345678, 12.86)
NOVEL_1 = MYTR.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 7.11)
NOVEL_1.set_isbn(9781536831139)
NONFICTION1 = MYTR.create_non_fiction( \
                "Automate the Boring Stuff", "Python", "beginner", 1929452, 24.75)
NONFICTION2 = MYTR.create_non_fiction(\
                "Computing Machinery and Intelligence", "AI", "advanced", 11111938, 0.01)
NOVEL_2 = MYTR.create_novel(\
                "The Diamond Age", "Neal Stephenson", 10101010, 12.71)
NOVEL_3 = MYTR.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 3.55)

#Create users:
MYTR.add_user("Alan Turing", "alan@turing.com")
MYTR.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
MYTR.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[BOOK_1, NOVEL_1, NONFICTION1])

#Add books to a user one by one, with ratings:
MYTR.add_book_to_user(BOOK_1, "alan@turing.com", 1)
MYTR.add_book_to_user(NOVEL_1, "alan@turing.com", 3)
MYTR.add_book_to_user(NONFICTION1, "alan@turing.com", 3)
MYTR.add_book_to_user(NONFICTION2, "alan@turing.com", 4)
MYTR.add_book_to_user(NOVEL_3, "alan@turing.com", 1)

MYTR.add_book_to_user(NOVEL_2, "marvin@mit.edu", 2)
MYTR.add_book_to_user(NOVEL_3, "marvin@mit.edu", 2)
MYTR.add_book_to_user(NOVEL_3, "david@computation.org", 4)

print("=========================")

#Uncomment these to test your functions:
print('Print Entire Catalog\n--------------------')
print(MYTR.print_catalog())
print("=========================")

print('Print all users\n---------------')
print(MYTR.print_users())
print("=========================")

print('Highest rated book:\n-------------------')
print(MYTR.highest_rated_book())
print("=========================")

print("Most read book:\n---------------")
print(MYTR.most_read_book())
print("=========================")

print("Most positive user:\n-------------------")
print(MYTR.most_positive_user())
print("=========================")

print("Top 3 books:\n------------")
print(MYTR.get_n_most_read_books(3))
print("=========================")

print("Top 2 most read users:\n---------------------")
print(MYTR.get_n_most_prolific_readers(2))
print("=========================")

print("Top 2 most expensive books:\n--------------------------")
print(MYTR.get_n_most_expensive_books(2))
print("=========================")

print("User Net Worth\n--------------")
for user in MYTR.users.values():
    print("Worth of {name} is ${worth}".format(
        name=user.name, worth=MYTR.get_worth_of_user(user.email)))
print("=========================")
