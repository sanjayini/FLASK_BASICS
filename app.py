'''

from flask import Flask 
app = Flask(__name__)   

@app.route('/') 
def sample(): 
    return 'Santhosh!' 

if __name__ == "__main__": 
    app.run()    
''' 


from flask import Flask, request
from redis import Redis
app = Flask(__name__)
@app.route('/')
def home():
    return 'Chennai'
@app.route('/country')
def get_country():
    return 'India'
@app.route('/ip')
def ip():
    ip_address = request.remote_addr
    return ip_address
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)