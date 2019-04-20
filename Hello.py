from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hell oh whirled !'

if __name__ == '__main__':
   app.run()