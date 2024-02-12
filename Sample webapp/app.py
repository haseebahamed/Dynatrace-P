from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to My Sample Web Application!</h1><p>This is a simple web application built with Python and Flask.</p>'

if __name__ == '__main__':
    app.run(debug=True)
