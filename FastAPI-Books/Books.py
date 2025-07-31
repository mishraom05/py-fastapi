from fastapi import FastAPI

app = FastAPI()

# Defining the list of Books
Books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'math'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'art'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'science'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'science-fiction'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'science'}
]

@app.get('/')
async def get_books():
    return {'books': 'All about books.'}

@app.get('/books')
async def get_books():
    return Books

@app.get("/books/{book_title}")
async def get_books_dynamic(book_title: str):
  for book in Books:
     if book.get('title').casefold() == book_title.casefold():
        return book

@app.get("/books/")
async def get_books_by_category(category: str):
    book_to_return = []
    for book in Books:
        if book.get('category') == category.casefold():
           book_to_return.append(book) 
    return book_to_return

@app.get("/books/{author}/")
async def get_books_dynamic_category(author: str, category: str):
    book_to_return = []
    for book in Books:
        if book.get('author').casefold() == author.casefold():
            if book.get('category') == category.casefold():
                book_to_return.append(book)
    return book_to_return
