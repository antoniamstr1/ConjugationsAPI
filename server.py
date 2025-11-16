from flask import Flask, request, jsonify
from verbix_sdk.v2 import get_conjugation, is_known_verb
import os
app = Flask(__name__)

# GET /verb?language=it&verb=andare


@app.route('/verb', methods=['GET'])
def conjugations():
    try:
        language = request.args.get('language')
        # italian-ita
        # spanish-spa
        language = {
            "it": "ita",
            "es": "spa"
        }.get(language)
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
