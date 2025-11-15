from flask import Flask, request, jsonify
from verbix_sdk.v2 import get_conjugation, is_known_verb

app = Flask(__name__)

# GET /verb?language=it&word=andare
@app.route('/verb', methods=['GET'])
def conjugations():
    try:
        language = request.args.get('language')
        verb = request.args.get('verb')
        if not language or not verb:
            return jsonify({"error": "Missing 'language' or 'verb' parameter"}), 400
        if (is_known_verb(language, verb)):
            return jsonify(get_conjugation(language, verb))
        else:
            return {}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)