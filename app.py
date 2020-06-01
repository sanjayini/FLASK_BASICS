from flask import Flask, request, jsonify
app = Flask(__name__) 
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/actor', methods = ['POST', 'GET'])
def hello_world():
    actor = request.args.get('actor') 
    actress = request.args.get('actress') 
    result = {
        "actor" : actor,
        "actress" : actress,
        "city" : "chennai",
        "state" : "tn"

    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True) 