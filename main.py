from flask import Flask, jsonify
import pandas as pd

arto_csv=pd.read_csv("shared_articles.csv")


app=Flask(__name__)

liked_article=[]
disliked_article=[]
all_articles=[]


@app.route('/liked_articles')
def liked_articles():
    return jsonify({
        "data":arto_csv,
        "status":"Success"
    })