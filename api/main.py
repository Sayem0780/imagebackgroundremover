from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
