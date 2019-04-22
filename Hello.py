from flask import Flask, redirect, url_for
app = Flask(__name__)

# index route
@app.route('/')
def home_page():
   return 'home page'

# route to hello world page
@app.route('/hello')
def hello_world():
   return 'hellooooo whirled!'

# dynamic route
@app.route('/<dynamicRoute>')
def dynamicHelloPage(dynamicRoute):
   return 'This is a page called %s' % dynamicRoute

# route with a dynamic integer
@app.route('/<int:idNumber>')
def dynamicIntegerPage(idNumber):
   return 'This is a page is number: %s' % idNumber


# example using url_for
@app.route('/admin')
def hello_admin():
   return 'Hello administrator'

@app.route('/guest/<guestName>')
def hello_guest(guestName):
   return 'Hi there %s, you are a guest.' % guestName


@app.route('/user/<username>')
def hello_user(username):

   # if user/admin is entered, then the hello_admin function will called
   if username == 'admin':
      return redirect(url_for('hello_admin'))

   # else the hello_guest function will be called and the guestname will be assigned the username
   else:
      return redirect(url_for('hello_guest', guestName = username))

if __name__ == '__main__':
   app.run(debug = True)