from flask import Flask, request
from redis import Redis

app = Flask(__name__)

@app.route('/')
def get_home_page():
    return 'Chennai'

@app.route('/country')
def get_country():
    return 'India'

@app.route('/ip')
def ip():
    ip_address = request.remote_addr
    return ip_address
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
'''

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/actor', methods = ['POST', 'GET'])
def hello_world():
    actor = request.args.get('actor') 
    actress = request.args.get('actress') 
    result = {
        "actor" : 'surya',
        "actress" : 'jyothika',
        "city" : "chennai",
        "state" : "tn"

    }
    return jsonify(result)


@app.route("/home")
def home():
  return render_template("home.html")
  
@app.route("/John")
def John():
  return "Hello John."

@app.route("/hello")
def hello():
    print(request.args['x'])
    return "Hello World!"

@app.route("/data/<section>")
def data(section):
    assert section == request.view_args['section']


app.add_url_rule('/', 'hello', 'hello_world')   

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest   

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))   

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)      


if __name__ == "__main__":
    app.run(debug = True)     
    