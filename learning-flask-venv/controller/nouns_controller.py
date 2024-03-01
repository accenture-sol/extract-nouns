from app import app
from flask import request, jsonify
from model import nouns_model

@app.route("/getNouns", methods=['POST'])
def extract_nouns_controller():
    data = request.get_json()
    noun_phrases = nouns_model.extract_noun_phrases(data['message'])
    return jsonify(noun_phrases)
        
