class Library:
    def __inti__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}


    def displayBooks(self):
        print(f"we have the following books in our libary: {self.name}") 
        for book in self.book.list:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():   
            self.lendDict.update({book:user})
            print("lender-Book database has been updated.you can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}") 

        def addBook(self, book):
            self.booklist.append(book)    
            print("book has been added to the book list ")

        def returnBook(self,book):
            self.lendDict.pop(book)    

        if __name__=='__main__':

          books = Library(['python', 'rich dad poor'])      