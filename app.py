from flask import Flask
import datetime

# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
app.route('/')
def index_page():
    return "Hello world"

app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.datetime.now())

# server the app when this file is run
if __name__ == '__main__':
    app.run()
