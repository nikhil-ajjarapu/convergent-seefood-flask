from flask import Flask, request, jsonify
from PIL import Image
from models.predict import predict_image

app = Flask(__name__)

@app.route("/")
def main_page_empty():
    return "<p>Server for SeeFood! Managed by Gilfoyle. (And Dinesh.) </p>"

# curl command (run from test data): 
# curl -v -F filename=dinesh.jpg -F upload=@dinesh.jpg http://localhost:5000/api/uploadPicture
# curl -v -F filename=seefood/test/hot_dog/133015.jpg -F upload=@seefood/test/hot_dog/133015.jpg http://localhost:5000/api/uploadPicture
@app.route("/api/uploadPicture", methods=['POST'])
def process_picture():
    files = request.files
    image = files.get('upload')
    img = Image.open(image)
    
    hotdog_status, prob = predict_image(img)

    return jsonify({
        "is_hotdog": hotdog_status,
        "probability": prob
    })
