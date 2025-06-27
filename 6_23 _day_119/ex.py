from flask import Flask, request, jsonify, send_file
import barcode
from barcode.writer import ImageWriter
import os

app = Flask(__name__)

@app.route('/generate-barcode', methods=['GET','POST'])
def generate_barcode():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    barcode_text = data['text']
    barcode_format = data.get('format', 'code128')  # Default to Code 128

    # Generate barcode
    try:
        barcode_class = barcode.get(barcode_format)
        barcode_instance = barcode_class(barcode_text, writer=ImageWriter())
        filename = f"{barcode_text}.png"
        barcode_instance.save(filename)

        return send_file(filename, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(filename):
            os.remove(filename)  # Clean up the generated file

if __name__ == '__main__':
    app.run(debug=True)
