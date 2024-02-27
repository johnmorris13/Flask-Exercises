from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    theTime=datetime.now().strftime('%A, %B %d %Y %H:%M:%S')
    return f'<h1>The current date time is {theTime} </h1>'

if __name__=="__main__":
    app.run(debug=True)