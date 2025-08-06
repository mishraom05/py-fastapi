# Database

## Installing sqlite3 on Windows

* [Installer](https://sqlite.org/2025/sqlite-tools-win-x64-3500400.zip)
* Extract the file in C:\\
* Save the path under `user environment variable`. 
* Sample path C:\\sqlite3

### Creating table in sqlite3 and performing database operations

* ToDos Table

|Id(PK)|title|description|priority|complete|owner(FK)|
|------|-----|-----------|--------|--------|---------|
|      |     |           |        |        |         |

### Inserting data into table

* To insert data into table use the `INSERT` statement

```sql
sqlite> INSERT INTO todos (title, description, priority, complete) VALUES ('Go to store', 'To pick up eggs', 5, False);
sqlite> INSERT INTO todos (title, description, priority, complete) VALUES ('Cut the lawn', 'grass is getting longer', 3, False);
sqlite> INSERT INTO todos (title, description, priority, complete) VALUES ('Feed the dog', 'Dog is hungry', 4, False);
```

### Fetching data from table

* To fetch all the data from the table `todos`

```sql
SELECT * FROM todos;
```

* OUTPUT

```sql
sqlite> select * from todos;
id  title         description              priority  complete
--  ------------  -----------------------  --------  --------
1   Go to store   To pick up eggs          5         0
2   Cut the lawn  grass is getting longer  3         0
3   Feed the dog  Dog is hungry            4         0
```

> [!NOTE]
> Boolean value `False` is represented as `0` in sql and `True` is represented as a `1`.

* To fetch the `title` from the `todos` table

### Different modes in sqlite3 to support output 

* There are 4 options to support the ouput in sqlite3
  * .mode column
  * .mode markdown
  * .mode box
  * .mode table

* OUTPUT

```sql
sqlite> .mode column
sqlite> select * from todos;
id  title         description              priority  complete
--  ------------  -----------------------  --------  --------
1   Go to store   To pick up eggs          5         0
2   Cut the lawn  grass is getting longer  3         0
3   Feed the dog  Dog is hungry            4         0

sqlite> .mode markdown
sqlite> select * from todos;
| id |    title     |       description       | priority | complete |
|----|--------------|-------------------------|----------|----------|
| 1  | Go to store  | To pick up eggs         | 5        | 0        |
| 2  | Cut the lawn | grass is getting longer | 3        | 0        |
| 3  | Feed the dog | Dog is hungry           | 4        | 0        |

sqlite> .mode box
sqlite> select * from todos;
┌────┬──────────────┬─────────────────────────┬──────────┬──────────┐
│ id │    title     │       description       │ priority │ complete │
├────┼──────────────┼─────────────────────────┼──────────┼──────────┤
│ 1  │ Go to store  │ To pick up eggs         │ 5        │ 0        │
│ 2  │ Cut the lawn │ grass is getting longer │ 3        │ 0        │
│ 3  │ Feed the dog │ Dog is hungry           │ 4        │ 0        │
└────┴──────────────┴─────────────────────────┴──────────┴──────────┘

sqlite> .mode table
sqlite> select * from todos;
+----+--------------+-------------------------+----------+----------+
| id |    title     |       description       | priority | complete |
+----+--------------+-------------------------+----------+----------+
| 1  | Go to store  | To pick up eggs         | 5        | 0        |
| 2  | Cut the lawn | grass is getting longer | 3        | 0        |
| 3  | Feed the dog | Dog is hungry           | 4        | 0        |
+----+--------------+-------------------------+----------+----------+
```

### List of other SQL queries

* To fetch the `title` from the `todos` table

```sql
SELECT title FROM todos;
```

* To fetch the `title` and `description` from the `todos` table

```sql
SELECT title,description FROM todos;
```

* To fetch the `title`, `description` and `priority` from the `todos` table

```sql
SELECT title,description,priority FROM todos;
```

### Using `WHERE` clause with `SELECT` statement

```sql
SELECT * WHERE PRIORITY=5 FROM todos;
```

### Update the `column` using `WHERE`

```sql
UPDATE todos SET complete=True WHERE id=5;
```

> [!NOTE]
> You can update the column `complete` by executing the below `UPDATE` query

```sql
UPDATE todos SET complete=True WHERE title='Learn something new';
```

> This method is not advisable as contents of column `title` is not unique.

### `DELETE` sql queries

* To DELETE all the rows WHERE id is equal to 5

```sql
DELETE FROM todos WHERE id=4;
```

* OUTPUT 

```sql
sqlite> select * from todos;
+----+--------------+-------------------------+----------+----------+
| id |    title     |       description       | priority | complete |
+----+--------------+-------------------------+----------+----------+
| 1  | Go to store  | To pick up eggs         | 5        | 0        |
| 2  | Cut the lawn | grass is getting longer | 3        | 0        |
| 3  | Feed the dog | Dog is hungry           | 4        | 0        |
| 4  | Test Element | Testing Description     | 4        | 0        |
+----+--------------+-------------------------+----------+----------+

sqlite> DELETE FROM todos WHERE id=4;
sqlite> select * from todos;
+----+--------------+-------------------------+----------+----------+
| id |    title     |       description       | priority | complete |
+----+--------------+-------------------------+----------+----------+
| 1  | Go to store  | To pick up eggs         | 5        | 0        |
| 2  | Cut the lawn | grass is getting longer | 3        | 0        |
| 3  | Feed the dog | Dog is hungry           | 4        | 0        |
+----+--------------+-------------------------+----------+----------+
```

> [!NOTE]
> You can delete the rows by executing the below `DELETE` query

```sql
DELETE FROM todos WHERE complete=0;
```

> This method is not advisable as the query has the potential to delete all rows of `todos` table. It is advised to use primary key field for the deletion purpose.
