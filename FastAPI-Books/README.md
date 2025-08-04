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

## Extending Use-Cases

### Pydantic

* Pydantic 1 vs Pydantic 2
* FastAPI is now compatible with both Pydantic v1 and Pydantic v2.
* Based on how new the version of FastAPI you are using, there could be small method name changes.
* The three biggest are:
  - .dict() function is now renamed to .model_dump()
  - schema_extra function within a Config class is now renamed to json_schema_extra
  - Optional variables need a =None example: id: Optional[int] = None

### What is pydantic?

* Create a different request model for data validation
* Field Data validation on each variable/element

```py
class BookRequest(BaseModel):
  id: int
  title: str = Field(min_length=3)
  author: str = Field(min_length=1, max_length=50)
  description: str = Field(min_length=1, max_length=100)
  rating: int = Field(gt=0, lt=6)
```

* Passing the BookRequest object onto the Book object

```py
@app.post('/create_books')
async def create_books(book_request: BookRequest):
  new_book = Book(**book_request.dict()) # ** <--- operator will pass the key/value from BookRequest into the Book's constructor
  Books.append(new_book)
```

* On passing the below json 

```json
{
  "id": 9,
  "title": "101-Oncology",
  "author": "Dr. James Wilson",
  "description": "Injecting Chemo to kill cells.",
  "rating": 4.1
}
```

* The error code received is `422` which is `Error: Unprocessable Entity`

```json
// Response Body
{
  "detail": [
    {
      "type": "int_from_float",
      "loc": [
        "body",
        "rating"
      ],
      "msg": "Input should be a valid integer, got a number with a fractional part",
      "input": 4.1
    }
  ]
}
```

* ModelConfig for configuring swagger to provide meaningful sample/example of json

```py
model_config = {
        "json_schema_extra":{
            "example":{
                "title": "101-Example",
                "author": "FName MName LName",
                "description": "A short and concise description",
                "rating": 4.9
            }
        }
    }
```

## Path and Query Parameters Data Validation

* Import Path and Query from fastapi to implement Path and Query parameters validation

```py
from fastapi import Body, FastAPI, Path, Query
```

* Add conditions using Path() and Query() methods to your apis for validation of data

```py
# Path Parameter 
@app.get('/books/get_books/{published_date}')
async def get_book_by_pub_date(pub_date: int = Path(gt=0, lt=2025)):
  pass

# Query Parameter
@app.get('/books/')
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
  pass
```

## Status Codes

* 1xx - Information Response: Request Processing
* 2xx - Successs: Request Successfully Complete
  * `200:OK` - Standard Response for a successful request. Commonly used for successful Get Requests when data is being returned.
  * `201:Created` - The request has been successful, creating a new resource. Used when a POST creates an entity.
  * `204:No Content` - The request has been successful, did not create an entity nor return anything. Commonly used with PUT requests.
* 3xx - Redirection: Further action must be complete
* 4xx - Client Errors: An error was caused by the client
  * `400:Bad Request` - Cannot process request due to client error. Commonly used for invalid request methods.
  * `401:Unauthorized` - Client does not have valid authentication for target resource.
  * `404:Not Found` - The clients requested resource can not be found.
  * `422:Unprocessable entity` - Semantic errors in client request.
  
  ```json
  /*
  422
  Error: Unprocessable Entity
  Response body
  */
  {
    "detail": [
      {
        "type": "greater_than",
        "loc": [
          "path",
          "book_id"
        ],
        "msg": "Input should be greater than 0",
        "input": "0",
        "ctx": {
          "gt": 0
        }
      }
    ]
  }
  ```

* 5xx - Server Errors: An error occured on the server
  * `500:Internal Server Error` - Generic error message, when an unexpected issue on the server happened.

### Raising Exception in code

* To raise an exception use the HTTPException()
* Sample code :

```py
from fastapi import HTTPException

@app.get('/books/{book_id}')
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in Books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item Not Found!')
```

* Sample Output if Input for `book_id` is `10` when book_id exists between 1-8.

```json
/*404
Undocumented
Error: Not Found
Response body
*/
{
  "detail": "Item Not Found!"
}
```

## Adding Status Code to the API's

* Adding custom HTTP code for the API endpoints.

```py
from starlette import status

# GET Request - Fetch details of all the books
@app.get('/books', status_code=status.HTTP_200_OK)

# POST Request - Create a new book        
@app.post('/books/create_book',status_code=status.HTTP_201_CREATED)
```
