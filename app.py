from flask import Flask, render_template, request, jsonify, send_file
import speech_recognition as sr
import io
from docx import Document
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribir', methods=['POST'])
def transcribir():
    if 'audio' not in request.files:
        return jsonify({'error': 'No se envió archivo de audio'}), 400
    
    audio_file = request.files['audio']
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
            audio_file.save(tmp.name)
            tmp_path = tmp.name
        
        recognizer = sr.Recognizer()
        with sr.AudioFile(tmp_path) as source:
            audio = recognizer.record(source)
        
        try:
            texto = recognizer.recognize_google(audio, language='es-ES')
            os.unlink(tmp_path)
            return jsonify({'texto': texto, 'exito': True})
        except sr.UnknownValueError:
            os.unlink(tmp_path)
            return jsonify({'error': 'No se pudo entender el audio', 'exito': False}), 400
        except sr.RequestError:
            os.unlink(tmp_path)
            return jsonify({'error': 'Error en el servicio de reconocimiento', 'exito': False}), 500
            
    except Exception as e:
        return jsonify({'error': str(e), 'exito': False}), 500

@app.route('/descargar/txt', methods=['POST'])
def descargar_txt():
    texto = request.json.get('texto', '')
    buffer = io.BytesIO()
    buffer.write(texto.encode('utf-8'))
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name='dictado.txt',
        mimetype='text/plain'
    )

@app.route('/descargar/docx', methods=['POST'])
def descargar_docx():
    texto = request.json.get('texto', '')
    doc = Document()
    doc.add_paragraph(texto)
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name='dictado.docx',
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

if __name__ == '__main__':
    app.run(debug=True)
