# Adding module translate to current directory
import sys
sys.path.insert(0, '../Transformers/')

# Turn off FutureWarning
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from translate import translate

app = Flask(__name__)
CORS(app)

# Khởi tạo Swagger
swagger = Swagger(app)

@app.route('/translate', methods=['POST'])
def translate_api():
    """
    Translate Text
    ---
    tags:
      - Translation
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - text
          properties:
            text:
              type: string
              description: Text to be translated
              example: "Hello"
    responses:
      200:
        description: Translation successful
        schema:
          type: object
          properties:
            Translated text:
              type: string
              description: Translated output
              example: "Bonjour"
      400:
        description: Input text is missing
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        input_text = data.get('text', '')

        if not input_text:
            return jsonify({"error": "No input text provided"}), 400

        translated_text = translate(input_text)

        return jsonify({'Translated text': translated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
