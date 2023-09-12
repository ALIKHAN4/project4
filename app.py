from flask import Flask 

app = Flask(__name__)

@app.route('/') #/ is a landing page
def home():
    return "<h1>Hello Python and Flask<h1>"
if __name__=="__main__":
    app.run(debug=True)

