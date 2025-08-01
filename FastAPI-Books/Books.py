from fastapi import Body,FastAPI

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

# GET Methods
@app.get('/')
async def get_books():
    return {'Books': 'All about books.'}

@app.get('/books')
async def get_all_books():
    return Books

@app.get("/books/{book_title}")
async def get_books_by_book_title(book_title: str):
  for book in Books:
     if book.get('title').casefold() == book_title.casefold():
        return book

@app.get("/books/by_author/")
async def get_books_by_author(author: str):
    book_to_return = []
    for book in Books:
        if book.get('author').casefold() == author.casefold():
           book_to_return.append(book) 
    return book_to_return

@app.get("/books/{author}/")
async def get_books_by_dynamic_category(author: str, category: str):
    book_to_return = []
    for book in Books:
        if book.get('author').casefold() == author.casefold():
            if book.get('category') == category.casefold():
                book_to_return.append(book)
    return book_to_return

@app.get("/books/")
async def get_books_by_category(category: str):
    book_to_return = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
           book_to_return.append(book) 
    return book_to_return

# POST Methods
@app.post('/books/create_book')
async def create_books(new_book=Body()):
    Books.append(new_book)

# PUT Methods
@app.put('/books/update_book')
async def update_books(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == updated_book.get('title').casefold():
            Books[i] = updated_book

# DELETE Methods
@app.delete('/books/delete_book/{book_title}')
async def delete_books(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books.pop(i)
            break
