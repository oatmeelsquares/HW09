import pandas as pd

class BookLover:

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = None):
        
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list == None:
            self.book_list = pd.DataFrame({
                "book_name" : [],
                "book_rating" : []
            })
        
        else:
            self.book_list = pd.DataFrame({
                "book_name" : book_list.keys(),
                "book_rating" : book_list.values()
            })


    def add_book(self, book_name, rating):

        new_book = pd.DataFrame({
            "book_name" : [book_name],
            "book_rating" : [rating]
        })

        if book_name not in self.book_list["book_name"].tolist():
            
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)

        else:

            print("That book is already in the list!")


    def has_read(self, book_name):

        return (book_name in self.book_list["book_name"].tolist())
    

    def num_books_read(self):

        return len(self.book_list)
    

    def fav_books(self):

        mask = self.book_list["book_rating"] > 3
        return self.book_list[mask]
    


if __name__ == "__main__":

    b = BookLover("Becky", "becky@becky.com", "Fantasy", 3, {"Ender's Game": 5, "Alcatraz vs. the Evil Librarians":5, "The Alchemist": 2})
    

#    print(b)

    b.add_book("Ender's Game", 5)
    b.add_book("Bad Book", 1)
    b.add_book("Some Title", 3)

    print(b.book_list)
#    print(b.fav_books())

#    print(b.book_list["book_name"])