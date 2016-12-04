from flask import Flask
from flask import render_template
import ConfigParser
import socket
import hisCinemaDNS

app = Flask(__name__)

configParser = ConfigParser.RawConfigParser()
configParser.read('config.py')

HOST = configParser.get('flask-config', 'hisCinema_HOST')
PORT = configParser.get('flask-config', 'hisCinema_PORT')
BUFFER_SIZE = 1024

# Pull up main page
@app.route("/")
def main():
    return render_template('index.html')

# Send to LocalDNS after client selects
@app.route("/get/<string:num>/")
def number(num):
	print "[DEBUG] Getting response from hisCinemaDNS"
	hisCinemaDNS.response(num);
	sendIP(num)
	return "Now downloading file: " + num + ".mp4"

def sendIP(num):
	hisCinemaDNS.response2()
	return "Now downloading file: " + num + ".mp4"

if __name__ == "__main__":
    app.run(HOST,PORT)
