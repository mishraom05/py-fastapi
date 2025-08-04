from typing import Optional
from fastapi import Body, FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

# Creating the class Book for storing Book objects
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# Inheriting from pydantic BaseModel for data validation
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=100)
    rating: float = Field(gt=0, lt=6)
    published_date: int = Field(gt=0, lt=2025)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "101-Example",
                "author": "FName MName LName",
                "description": "A short and concise description",
                "rating": 4.9,
                "published_date": 2020
            }
        }
    }
    
# Creating Book objects and storing it in a list
Books = [
    Book(1, '101-Computer Science', 'Charles Babbage', 'Understanding mystery of Computer Science', 4, 1987),
    Book(2, '101-Science', 'Charles Darwin', 'Unravelling mysteries of Science', 5, 1836),
    Book(3, '101-Mathematics', 'Srinivasan Ramanujan', 'Calculus is magic!', 5, 1820),
    Book(4, '101-History', 'Charles Ram', 'History as it was, not what\'s spoken', 2, 1600),
    Book(5, '101-Art', 'Leonardo Da Vinci', 'Monalisa, through my eyes', 3, 600)
]

# Get methods for fetching book(s)
@app.get('/books', status_code=status.HTTP_200_OK)
async def read_all_books():
    return Books

@app.get('/books/{book_id}', status_code=status.HTTP_200_OK) 
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in Books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item Not Found!')

@app.get('/books/', status_code=status.HTTP_200_OK)
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    book_lst = []
    for book in Books:
        if book.rating == book_rating:
            book_lst.append(book)
    if len(book_lst) > 0:
        return book_lst
    else:
        raise HTTPException(status_code=404, detail='Item Not Found!')

@app.get('/books/get_books/{published_date}', status_code=status.HTTP_200_OK)
async def get_book_by_pub_date(pub_date: int = Path(gt=0, lt=2025)):
    book_lst = []
    for book in Books:
        if book.published_date == pub_date:
            book_lst.append(book)
    if len(book_lst) > 0:
        return book_lst
    else:
        raise HTTPException(status_code=404, detail='Item Not Found!')
    

# POST Request - Create a new book        
@app.post('/books/create_book',status_code=status.HTTP_201_CREATED)
async def create_books(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(get_book_id(new_book))

def get_book_id(book: Book):

    # Implementing ternary operator instead of if else block
    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    # if len(Books) > 0:
    #     book.id = Books[-1].id + 1
    # else:
    #     book.id = 1
    return book

# PUT method to update a book
@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i in range(len(Books)):
        if Books[i].id == book.id:
            Books[i] = Book(**book.model_dump())
            return Books[i]
    raise HTTPException(status_code=404, detail="Error! Book not found.")

# DELETE method to delete a book
@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_count=len(Books)
    for i in range(book_count):
        if Books[i].id == book_id:
            Books.pop(i)
            return {"200": "Book Deleted!"}
    raise HTTPException(status_code=404, detail='Item Not Found!')