# Books Project Overview

* Creating an API that will display information related to books.
* Basic CRUD operation :
  - Create - POST the list of books.
  - Request - GET the list of books.
  - Update - PUT the list the books.
  - Delete - DELETE the list of books.

## Starting the uvicorn server

* .\venv\Scripts\fastapi.exe dev Books.py - Runs the server in Development Mode.
* .\venv\Scripts\fastapi.exe run Books.py - Runs the server in Production Mode.
* uvicorn.exe Books:app --reload - - Runs the server in Production Mode.

## Path Parameters

* Path Parameters are request parameters that have been attached to the URL.
* Path Parameters are usually defined as a way to find information based on location.
* Think of a computer file system.
  - You can identify the specific resources based on the file you are in:
  - */Users/username/Documents/python/fastapi/section1*

```py
@app.get("/books/{dynamic_param}")
async def get_books_dynamic(dynamic_param):
  return {'dynamic_param': dynamic_param}
```

* FastAPI parses the list of APIs in chronological order.
* Dynamic Path Parameter should be defined at the end so that it acts as the function to fallback on if no endpoint matches.

```py
@app.get("/books/book_one") #<-------(1)
async def get_books():
    return Books

@app.get("/books/{dynamic_param}") #<----------(2)
async def get_books_dynamic(dynamic_param):
  return {'dynamic_param': dynamic_param}
```

* URL : https://domain_name/books/book_one will redirect to function (1)
* URL : https://domain_name/books/book_two or any other param except `book_one` will redirect to function (2)
* In the URL `http://127.0.0.1:8000/books/title%20two`, `%20` equals space.

## Query Parameters

* Query Parameters are request parameters that have been attached after a "?"
* Query Parameters have name=value pairs
* Example:
  - [http://127.0.0.1:8000/books/?category=science](http://127.0.0.1:8000/books/?category=science)

```json
[
  {
    "title": "Title One",
    "author": "Author One",
    "category": "science"
  },
  {
    "title": "Title Four",
    "author": "Author Four",
    "category": "science"
  },
  {
    "title": "Title Six",
    "author": "Author Two",
    "category": "science"
  }
]
```
