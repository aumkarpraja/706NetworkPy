from flask import Flask
from flask import render_template
import ConfigParser


app = Flask(__name__)

configParser = ConfigParser.RawConfigParser()
configParser.read('config.py')

HOST = configParser.get('flask-config', 'hisCinema_HOST')
PORT = configParser.get('flask-config', 'hisCinema_PORT')
BUFFER_SIZE = 1024

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":

    app.run(HOST,PORT)
