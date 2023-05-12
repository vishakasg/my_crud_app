from flask import render_template, request, redirect
from models.user import create_user

def new():
  return render_template('users/new.html')

def create():
  first_name = request.form.get('first_name')
  last_name = request.form.get('last_name')
  address = request.form.get('address')
  email = request.form.get('email')
  password = request.form.get('password')
  create_user(first_name, last_name, address,  email, password)
  return redirect('/')
