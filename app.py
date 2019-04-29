from flask import Flask, render_template, redirect, url_for
from data import Articles

# Creating an instance of the Flask class
app = Flask(__name__)

# creating a variable Articles and setting it equal to the Articles function
Articles = Articles()

# home page route
@app.route('/')
def index():
   return render_template('home.html')

# route to about page
@app.route('/about')
def about():
   return render_template('/about.html')

@app.route('/articles')
def articles():
   # adding a parameter (articles) to pass in the data (Articles)
   return render_template('/articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
   return render_template('/article.html', id = id)

if __name__ == '__main__':
   # debug = True will automatically restart the server when changes are made
   app.run(debug = True)