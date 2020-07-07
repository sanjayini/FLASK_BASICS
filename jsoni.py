from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

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

@app.route('/_get_current_user')
def get_current_user():
    result = {
        "username" : 'username',
        "email" : 'email',
        "id" : 'id'
    }    

    return jsonify(result)               



if __name__ == "__main__":
    app.run(debug = True) 