from flask import Flask, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    print(request.args['x'])
    return "Hello World!"

@app.route("/data/<section>")
def data(section):
    assert section == request.view_args['section']


if __name__ == "__main__":
    app.run()