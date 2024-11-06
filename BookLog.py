class Book_log:

  def __init__(self,bookname,authorname,genre,no_of_pages,price):
    self.bookname = bookname
    self.authorname = authorname
    self.genre = genre
    self.no_of_pages = no_of_pages
    self.price = price


  def display(self):
    print("Book Name = ",self.bookname)
    print("Author name = ",self.authorname)
    print("Book Genre = ",self.genre)
    print("No_Of_Pages = ",self.no_of_pages)
    print("Book Price = ",self.price)


book1 = Book_log("The Silent Patient","Alex Michaelides","Psychological Thriller",336,11.99)
book2 = Book_log("The Midnight Library","Matt Haig","Science Fiction",288,11.99)
book3 = Book_log("Educated","Tara Westover","Memoir, Non-fiction",352,12.99)
book4 = Book_log("The Alchemist","Paulo Coelho","Fiction, Inspirational",208,9.99)
book5 = Book_log("Becoming","Michelle Obama","Memoir, Autobiography",448,15.99)


book1.display()
print()
book2.display()
print()
book3.display()
print()
book4.display()
print()
book5.display()
print()
