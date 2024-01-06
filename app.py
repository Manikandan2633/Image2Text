from flask import Flask, render_template, request,jsonify
import pytesseract
from PIL import Image
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith(('.jpg', '.png', '.jpeg')):
            image_text = extract_text_from_image(file)
            return render_template('index.html', text=image_text)
        else:
            return "Unsupported file format"



def extract_text_from_image(image_file):
    img = Image.open(image_file)
    pytesseract.pytesseract.tesseract_cmd =r'C:\Users\Programs\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img)
    text = pytesseract.image_to_string(img)
    return text







translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        data = request.get_json()
        text = data['text']
        target_language = data['language']

        translated_text = translator.translate(text, dest=target_language).text
        return jsonify({'translated_text': translated_text})



if __name__ == '__main__':
    app.run(debug=True)
