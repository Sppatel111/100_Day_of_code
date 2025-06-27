from flask import Flask, request, jsonify
import PyPDF2
import pyttsx3
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_speech():

    file = request.files['file']

    if file and file.filename.endswith('.pdf'):
        text = ''
        try:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        except Exception as e:
            return jsonify({'error': f'Error reading PDF: {str(e)}'}), 500

        try:
            speak = pyttsx3.init()
            audio_file_path = 'output_audio.mp3'
            speak.save_to_file(text, audio_file_path)
            speak.runAndWait()
            return jsonify({'message': 'Audio generated successfully', 'audio_file': audio_file_path}), 200
        except Exception as e:
            return jsonify({'error': f'Error during text-to-speech conversion: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Invalid file type. Please upload a PDF file.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
