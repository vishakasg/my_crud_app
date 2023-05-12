CREATE DATABASE online_gift_portal_db;
\c online_gift_portal_db

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name TEXT,
    image_url TEXT, 
    type TEXT,
    quantity TEXT, 
    price TEXT, 
    description TEXT
);

INSERT INTO products(name, image_url, type, quentity, price, description)
VALUES


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    address TEXT,
    email TEXT,
    password_digest TEXT
);

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  product_id INTEGER
);

CREATE TABLE reviews(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  product_id INTEGER
);


CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    user_id INTEGER;
    date TEXT,
    items TEXT,
    delivary_address TEXT,
    total_amount TEXT

);

CREATE TABLE carts(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER
);
