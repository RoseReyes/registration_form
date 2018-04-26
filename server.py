from flask import Flask, render_template, redirect, request,session,flash
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/') #This is the root
def landing_page():
  return render_template('index.html')  

@app.route('/result', methods=['POST']) 
def result():
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  email = request.form['email']
  pwd = request.form['pwd']
  pwdConfirm = request.form['pwdConfirm']
  
  if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(pwd) < 1 or len(pwdConfirm) < 1:
     flash("All fields are required.") 
  if first_name.isdigit() or last_name.isdigit():
      flash("First name or Last name should not contain any numbers")
  if not EMAIL_REGEX.match(session['email']):
      flash("Invalid Email Address!")
  if len(pwd) < 8 or len(pwd) > 8:
      flash("Password should be 8 characters long")
  if pwd != pwdConfirm:
      flash("Passwords does not match")
  else:
      return redirect('/')
app.run(debug=True) 