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

## GET Request

* A GET Request is used to fetch the data that is currently stored.
* To fetch the data based on a specific parameter that is passed in the URL, `dynamic_param` is used.

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

## POST Request

* This is used to create data
* POST can have a body that has additional information that GET does not have.
* Example of Body

```json
{
  "title": "Title Seven",
  "author": "Author One",
  "category": "science"
}
```

* Sample POST Request

```py
@app.post('/books/create_book')
async def create_books(new_book=Body()):
    Books.append(new_book)
```

## PUT Request

* A PUT request is used to update the data.
* PUT can have a body that has additional information (like POST) that GET does not have.
* Example of Body

```json
// Original Values
{
  "title": "Title Seven",
  "author": "Author One",
  "category": "science"
}

// Updated value passed in PUT Request
{
  "title": "Title Seven",
  "author": "Author One",
  "category": "math"
}
```

* Sample PUT Request

```py
@app.put('/books/update_book')
async def update_books(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == updated_book.get('title').casefold():
            Books[i] = updated_book
```

## DELETE Request

* A DELETE request is used to delete data.

```yaml
http://127.0.0.1:8000/books/delete_book/{book_title}
```

* Sample DELETE Request

```py
@app.delete('/books/delete_book/{book_title}')
async def delete_books(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books.pop(i)
            break
```
