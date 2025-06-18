import os
import whisper
import ffmpeg
from flask import Flask, request, render_template, send_file
from fpdf import FPDF
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PDF_FOLDER'] = 'pdfs'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PDF_FOLDER'], exist_ok=True)

# Load Whisper model once
model = whisper.load_model("base")

def extract_audio(video_path, audio_path):
    # Use ffmpeg to extract audio (MP3 format)
    ffmpeg.input(video_path).output(audio_path, acodec='mp3').run(overwrite_output=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No file part", 400

    video_file = request.files['video']
    if video_file.filename == '':
        return "No selected file", 400

    filename = secure_filename(video_file.filename)
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    video_file.save(video_path)

    # Extract audio
    audio_path = video_path.rsplit('.', 1)[0] + '.mp3'
    extract_audio(video_path, audio_path)

    # Transcribe
    result = model.transcribe(audio_path)
    os.remove(audio_path)

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Subtitles Extracted from Video", ln=True, align="C")
    pdf.ln(10)

    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        text = segment['text'].strip()
        line = f"[{start:.2f} - {end:.2f}] {text}"
        pdf.multi_cell(0, 10, line)

    pdf_filename = os.path.splitext(filename)[0] + '_subtitles.pdf'
    pdf_path = os.path.join(app.config['PDF_FOLDER'], pdf_filename)
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
