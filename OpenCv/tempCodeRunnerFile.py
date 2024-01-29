from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the background removal API!'

# Add the <image> variable to the route decorator
@app.route('/bgremove/<image>', methods=['POST'])
def bgremove(image):
    # Get the image file from the request
    image_file = request.files[image]
    # Convert the image file to bytes
    image_bytes = image_file.read()
    # Remove the background using rembg
    bgimg_bytes = remove(image_bytes)
    # Convert the bytes to a PIL image
    bgimg = Image.open(io.BytesIO(bgimg_bytes))
    # Save the image to a temporary file
    temp_file = io.BytesIO()
    bgimg.save(temp_file, format='PNG')
    # Return the file as a response
    temp_file.seek(0)
    return send_file(temp_file, mimetype='image/png')

if __name__ == '__main__':
    app.run()
