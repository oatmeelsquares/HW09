import pandas as pd
from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # Initialize an instance
        b = BookLover("Becky", "becky@becky.com", "Fantasy")
        b.add_book("Ender's Game", 5)


        # Run test
        assert "Ender's Game" in b.book_list["book_name"].tolist(), "The book wasn't added"


    def test_2_add_book(self):
        # Initialize an instance
        b = BookLover("Becky", "becky@becky.com", "Fantasy")
        b.add_book("Ender's Game", 5)
        b.add_book("Bad Book", 1)
        b.add_book("Some Title", 3)
        b.add_book("Ender's Game", 5)

        # Run test
        books = b.book_list["book_name"].tolist()
        assert books.count("Ender's Game") == 1, "duplicate book added"


    def test_3_has_read(self):
        # Initialize an instance
        b = BookLover("Becky", "becky@becky.com", "Fantasy")
        b.add_book("Ender's Game", 5)
        b.add_book("Bad Book", 1)
        b.add_book("Some Title", 3)

        # Run test
        assert b.has_read("Ender's Game") == True, "has_read failed to return true for a book in the list" 

    
    def test_4_has_read(self):
        # Initialize an instance
        b = BookLover("Becky", "becky@becky.com", "Fantasy")
        b.add_book("Ender's Game", 5)
        b.add_book("Bad Book", 1)
        b.add_book("Some Title", 3)

        # Run test
        self.assertFalse(b.has_read("The Chronicles of Narnia"), "has_read returned true for a book not in the list")
 

    def test_5_num_books_read(self):
        # Initialize an instance
        b = BookLover("Becky", "becky@becky.com", "Fantasy")
        b.add_book("Ender's Game", 5)    
        b.add_book("Bad Book", 1)
        b.add_book("Some Title", 3)

        # Run test
        assert b.num_books_read() == 3, "num_books_read returned the wrong number" 


    def test_6_fav_books(self):
        # Initialize an instance
        b = BookLover("Becky", "becky@becky.com", "Fantasy")
        b.add_book("Ender's Game", 5)    
        b.add_book("Bad Book", 1)
        b.add_book("Some Title", 3)
        b.add_book("Unbroke Horses", 4)

        # Run test
        ratings = b.fav_books()["book_rating"].tolist()

        for rating in ratings:
            assert rating > 3, "Rating below 3 in fav_books" 
        
        

if __name__ == "__main__":

    unittest.main(verbosity = 3)