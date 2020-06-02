


from flask import Flask 
app = Flask(__name__)   

@app.route('/') 
def sample(): 
    return 'Santhosh!' 

if __name__ == "__main__": 
    app.run()    