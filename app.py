# app.py
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from vision_model import generate_caption, answer_question

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    caption = None
    answer = None
    image_url = None
    question_asked = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        # This is the crucial line that grabs your question!
        question = request.form.get('question', '').strip()
        
        if file.filename == '':
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            image_url = filepath
            caption = generate_caption(filepath)
            
            # This is the crucial block that runs the VQA model!
            if question:
                answer = answer_question(filepath, question)
                question_asked = question
            
    return render_template('index.html', caption=caption, answer=answer, image_url=image_url, question_asked=question_asked)

if __name__ == '__main__':
    app.run(debug=True, port=5000)