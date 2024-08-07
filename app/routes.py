from app import app
from flask import request, render_template, redirect, url_for
import pickle
from werkzeug.utils import secure_filename
import os

class DummyModel:
    def predict(self, filepath):
        return "Healthy"

model = DummyModel()
try:
    model = pickle.load(open('app/model/disease_model.pkl', 'rb'))
except:
    pass

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        prediction = model.predict(filepath)
        return render_template

