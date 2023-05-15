from flask import render_template, request, redirect, session
from models.product import all_products, get_product, create_product, update_product, delete_product, create_review
from services.session_info import current_user

def index():
  products = all_products()
  return render_template('products/index.html', products=products, current_user=current_user)

def new():
  return render_template('products/new.html')

def create():
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  type = request.form['catagory']
  quantity = request.form.get('quantity')
  price = request.form.get('price')
  description = request.form.get('description')
  create_product(name, image_url, type, quantity, price, description)
  return redirect('/')

def edit(id):
  product = get_product(id)
  return render_template('products/edit.html', product=product)

def update(id):
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  type = request.form.get('type')
  quantity = request.form.get('quantity')
  price = request.form.get('price')
  description = request.form.get('description')
  update_product(id, name, image_url, type, quantity, price, description)
  return redirect('/')

def delete(id):
  delete_product(id)
  return redirect('/')

def reviews(id):
  product = get_product(id)
  return render_template('/products/reviews.html', product=product, current_user=current_user())

def write_review(id):
  product_id = id
  user_id = session['user_id']
  review = request.form.get('review')
  create_review( product_id, user_id, review)
  return redirect('/')

# def display_review(id):
#   product = get_product(id)
#   return render_template('/products/review.html', product=product, current_user=current_user())


