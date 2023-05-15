from db.db import sql

def all_products():
  return sql('SELECT * FROM products ORDER BY type')

def get_product(id):
  products = sql("SELECT * FROM products WHERE id = %s", [id])
  return products[0]

def create_product(name, image_url, type, quantity, price, description):
  sql('INSERT INTO products(name, image_url, type, quantity, price, description) VALUES(%s, %s, %s, %s, %s, %s) RETURNING *', [name, image_url, type, quantity, price, description])

def update_product( id, name, image_url, type, quantity, price, description):
  sql('UPDATE products SET name=%s, image_url=%s, type=%s, quantity=%s, price=%s, description=%s WHERE id=%s RETURNING *', [name, image_url, type, quantity, price, description, id])

def delete_product(id):
  sql('DELETE FROM products WHERE id=%s RETURNING *', [id])

def create_review(product_id, user_id, review):
  sql('INSERT INTO reviews(product_id, user_id, review) VALUES(%s, %s, %s) RETURNING *', [product_id, user_id, review])

# def get_reviews(id):
#   sql("SELECT * FROM products WHERE id = %s", [id])

# def display_reviews():
#   sql("SELECT * FROM reviews WHERE id = %s", [id])
  
