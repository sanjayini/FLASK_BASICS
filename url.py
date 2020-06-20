from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'
   


if __name__ == '__main__':
   app.run(debug = True)   