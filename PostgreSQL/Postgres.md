# PostgreSQL


## INSTALL
Download PostgreSQL 
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Components 
- PostgreSQL Server 
- pgAdmin 4
- Command Line Tools 

START
SQL Shell (psql) 
Command Line 

Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:

SELECT version();


pgAdmin

Servers > Databases > postgres 

Right click on "postgres" and select "Query Tool"  

SELECT version(); and click "Execute Script (F5)"  Play button 

---------------------------------------------------------------------------
## SQL Shell (psql) 
Command Line 

### Find all users
\du
\du+

### Create a user 
createuser testuser

### List all databases
SELECT datname FROM pg_database;

### Create a database
created testdb


### Connect to a database 
\connect my_database
\c my_database

### List tables
\dt


CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);

INSERT INTO cars (brand, model, year)
VALUES ('Ford', 'Mustang', 1964);

INSERT INTO cars (brand, model, year)
VALUES
  ('Volvo', 'p1800', 1968),
  ('BMW', 'M1', 1978),
  ('Toyota', 'Celica', 1975);


### FETCH DATA
SELECT * FROM cars;
SELECT brand, year FROM cars;


### ADD COLUMN
ALTER TABLE cars ADD color VARCHAR(255);


### UPDATE 
UPDATE cars SET color = 'red' WHERE brand = 'Volvo';

Change the year column from INT to VARCHAR(4):
ALTER TABLE cars ALTER COLUMN year TYPE VARCHAR(4);

Change the color column from VARCHAR(255) to VARCHAR(30):
ALTER TABLE cars ALTER COLUMN color TYPE VARCHAR(30);


### DROP COLUMN
ALTER TABLE cars DROP COLUMN color;


### DELETE
Delete all records where brand is 'Volvo':
DELETE FROM cars WHERE brand = 'Volvo';


### DROP TABLE 
DROP TABLE cars;




### OPERATORS 
WHERE Clause

=	Equal to						WHERE brand = 'Volvo';
<	Less than						WHERE year < 1975;
>	Greater than
<=	Less than or equal to					WHERE year <= 1975;
>=	Greater than or equal to				WHERE year >= 1975;
<>	Not equal to						WHERE brand <> 'Volvo';
!=	Not equal to						WHERE brand != 'Volvo';
LIKE	Check if a value matches a pattern (case sensitive)
ILIKE	Check if a value matches a pattern (case insensitive)
AND	Logical AND						WHERE brand = 'Volvo' AND year = 1968;
OR	Logical OR						WHERE brand = 'Volvo' OR year = 1975;
IN	Check if a value is between a range of values		WHERE brand IN ('Volvo', 'Mercedes', 'Ford');
BETWEEN	Check if a value is between a range of values		WHERE year BETWEEN 1970 AND 1980;
IS NULL	Check if a value is NULL				WHERE model IS NULL;
NOT	Makes a negative result e.g. NOT LIKE, NOT IN, NOT BETWEEN


### LIKE 
The percent sign %, represents zero, one, or multiple characters.
The underscore sign _, represents one single character.

STARTS with a capital 'M':	
WHERE model LIKE 'M%';
WHERE model ILIKE 'm%';


### NOT 
The NOT operator can be used together with LIKE, ILIKE, IN, BETWEEN, and NULL operators to reverse the truth of the operator.
WHERE brand NOT LIKE 'B%';
WHERE brand NOT ILIKE 'b%';
WHERE brand NOT IN ('Volvo', 'Mercedes', 'Ford');
WHERE year NOT BETWEEN 1970 AND 1980;
WHERE model IS NOT NULL;


### SELECT 
SELECT customer_name, country FROM customers;
SELECT DISTINCT country FROM customers;
SELECT COUNT(DISTINCT country) FROM customers;



### ORDER BY 
ORDER BY price;
ORDER BY price DESC;

ALPHABETICALLY
ORDER BY product_name;
ORDER BY product_name DESC;


### LIMIT 
SELECT * FROM customers LIMIT 20;


### OFFSET
Return 20 records, starting from the 41th record:
SELECT * FROM customers LIMIT 20 OFFSET 40;

### MIN 
Return the lowest price in the products table:
SELECT MIN(price) FROM products;

### MAX
The MAX() function returns the largest value of the selected column.
SELECT MAX(price) FROM products;

### SET COLUMN NAME
Return the lowest price, and name the column lowest_price:
SELECT MIN(price) AS lowest_price FROM products;

### COUNT
SELECT COUNT(customer_id) FROM customers;
SELECT COUNT(customer_id) FROM customers WHERE city = 'London';


### SUM
SELECT SUM(quantity) FROM order_details;

### AVG
SELECT AVG(price) FROM products;

### DECIMALS
SELECT AVG(price)::NUMERIC(10,2) FROM products;


### LIKE
SELECT * FROM customers WHERE customer_name LIKE 'A%';

### CONTAINS
SELECT * FROM customers WHERE customer_name LIKE '%A%';
SELECT * FROM customers WHERE customer_name ILIKE '%A%';
SELECT * FROM customers WHERE customer_name LIKE '%en';

SELECT * FROM customers WHERE city LIKE 'L_nd__';


### IN
SELECT * FROM customers WHERE country IN ('Germany', 'France', 'UK');


NOT IN
SELECT * FROM customers WHERE country NOT IN ('Germany', 'France', 'UK');

### IN (SELECT)
SELECT * FROM customers WHERE customer_id IN (SELECT customer_id FROM orders);
NOT IN (SELECT)
SELECT * FROM customers WHERE customer_id NOT IN (SELECT customer_id FROM orders);


### BETWEEN
SELECT * FROM Products WHERE Price BETWEEN 10 AND 15;

SELECT * FROM orders WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05';

The result returns all records that are alphabetically between the specified values.
SELECT * FROM Products WHERE product_name BETWEEN 'Pavlova' AND 'Tofu';
SELECT * FROM Products WHERE product_name BETWEEN 'Pavlova' AND 'Tofu' ORDER BY product_name;
All products that starts with p, Q, R, S, T


### AS
SELECT customer_id AS id FROM customers;
AS is Optional
SELECT customer_id id FROM customers;


### Concatenate Columns ||
two or more fields are concatenated into one
SELECT product_name || unit AS product FROM products;
SELECT product_name || ' ' || unit AS product FROM products;
SELECT product_name AS "My Great Products" FROM products;


## JOINS


## INNER JOIN
Only the records with a match in BOTH tables are returned:
SELECT product_id, product_name, category_name FROM products
INNER JOIN categories ON products.category_id = categories.category_id;


## LEFT JOIN
ALL records from the "left" table, and the matching records from the "right" table.
SELECT testproduct_id, product_name, category_name FROM testproducts
LEFT JOIN categories ON testproducts.category_id = categories.category_id;


## RIGHT JOIN
ALL records from the "right" table, and the matching records from the "left" table. 
SELECT testproduct_id, product_name, category_name FROM testproducts
RIGHT JOIN categories ON testproducts.category_id = categories.category_id;


## FULL JOIN
ALL records from both tables, even if there is not a match. 
SELECT testproduct_id, product_name, category_name FROM testproducts
FULL JOIN categories ON testproducts.category_id = categories.category_id;


## CROSS JOIN
matches ALL records from the "left" table with EACH record from the "right" table.
That means that all records from the "right" table will be returned for each record in the "left" table.



## UNION
combine the result-set of two or more queries.
Rules
- They must have the same number of columns
- The columns must have the same data types
- The columns must be in the same order

SELECT product_id FROM products
UNION
SELECT testproduct_id FROM testproducts
ORDER BY product_id;


### UNION ALL
returns duplicate values.
SELECT product_id FROM products
UNION ALL
SELECT testproduct_id FROM testproducts
ORDER BY product_id;


### GROUP BY 
groups rows that have the same values into summary rows, 
like "find the number of customers in each country".

often used with aggregate functions like COUNT(), MAX(), MIN(), SUM(), AVG()

SELECT COUNT(customer_id), country FROM customers
GROUP BY country;


SELECT customers.customer_name, COUNT(orders.order_id) FROM orders
LEFT JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customer_name;


3## HAViNG 

The HAVING clause was added to SQL because the WHERE clause cannot be used with aggregate functions.
Aggregate functions are often used with GROUP BY clauses,

SELECT COUNT(customer_id), country FROM customers
GROUP BY country
HAVING COUNT(customer_id) > 5;


SELECT order_details.order_id, SUM(products.price) FROM order_details
LEFT JOIN products ON order_details.product_id = products.product_id
GROUP BY order_id
HAVING SUM(products.price) > 400.00;


SELECT customers.customer_name, SUM(products.price) FROM order_details
LEFT JOIN products ON order_details.product_id = products.product_id
LEFT JOIN orders ON order_details.order_id = orders.order_id
LEFT JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customer_name
HAVING SUM(products.price) > 1000.00;

What is the primary purpose of the HAVING clause?
To filter groups based on an aggregate condition after grouping


### EXISTS
The EXISTS operator is used to test for the existence of any record in a sub query.
returns TRUE if the sub query returns one or more records.

SELECT customers.customer_name
FROM customers
WHERE EXISTS (
  SELECT order_id
  FROM orders
  WHERE customer_id = customers.customer_id
);


### NOT EXISTS
SELECT customers.customer_name
FROM customers
WHERE NOT EXISTS (
  SELECT order_id
  FROM orders
  WHERE customer_id = customers.customer_id
);


### ANY
The ANY operator allows you to perform a comparison between a single column value and a range of other values.
Returns Boolean , TRUE if ANY of the sub query values meet the condition

SELECT product_name
FROM products
WHERE product_id = ANY (
  SELECT product_id
  FROM order_details
  WHERE quantity > 120
);


### ALL 
is used with SELECT, WHERE and HAVING statements
returns TRUE if ALL of the sub query values meet the condition

SELECT product_name
FROM products
WHERE product_id = ALL (
  SELECT product_id
  FROM order_details
  WHERE quantity > 10
);


### CASE
The CASE expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement).
Once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause.
If there is no ELSE part and no conditions are true, it returns NULL.

SELECT product_name,
CASE
  WHEN price < 10 THEN 'Low price product'
  WHEN price > 50 THEN 'High price product'
ELSE
  'Normal product'
END
FROM products;




### WITH AN ALIAS 
When a column name is not specified for the "case" field, the parser uses case as the column name.
To specify a column name, add an alias after the END keyword.


SELECT product_name,
CASE
  WHEN price < 10 THEN 'Low price product'
  WHEN price > 50 THEN 'High price product'
ELSE
  'Normal product'
END AS "price category"
FROM products;






















