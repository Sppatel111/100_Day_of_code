import os.path
from flask import Flask, request, jsonify, send_file
import barcode
from barcode.writer import ImageWriter

app = Flask(__name__)

data = {
    "text": "123456789009"
}

@app.route('/generate', methods=['GET', 'POST'])
def generate_barcode():
    data = request.json
    if 'text' not in data or not data:
        return jsonify({'error': 'No text provided'})

    barcode_text = data['text']
    barcode_format = data.get('format', 'code128')

    try:
        barcode_class = barcode.get(barcode_format)
        barcode_instance = barcode_class(barcode_text, writer=ImageWriter())
        file_name = f'{barcode_text}'
        barcode_instance.save(file_name)

        headers = {
            'Content-Disposition': f'attachment; filename={file_name}',
            'X-Generated-By': 'Flask Barcode Generator'

        }

        return send_file(file_name, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)


if __name__ == '__main__':
    app.run(debug=True)

# postman checked

import scipy.datasets
import pooch