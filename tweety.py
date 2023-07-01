from flask import Flask, jsonify, request
import torch
from transformers import pipeline
from flask_cors import CORS, cross_origin


app = Flask("name")
api_v1_cors_config = {
    "origins": ["*"], 
    "methods": ["OPTIONS", 'GET', 'POST'], 
    "allow_headers": ["Authorization", "Content-Type"]
}

CORS(app, resources={r"/*" : api_v1_cors_config})

#determine app route 
@app.route('/sentiment_analysis', methods = ['POST'])
@cross_origin(**api_v1_cors_config)
def sentiment_analysis():
    print(request.json)
    print("above is the JSON")


    input_data = request.json.get('input')
    sentiment_task = pipeline( model="finiteautomata/bertweet-base-sentiment-analysis")
   # returns pos/neg/neu + score 
    result = sentiment_task(input_data)[0]
    print(result)
    print("THIS IS DA RESULT ABOVE")
    return jsonify({'result': result})

@app.get('/bruh')
def bruh(): 
    return "bruh moment"

if __name__ =="__main__":
    app.run(debug=True, port=3000)