from app import app

from flask import jsonify,request, Response
from .services.BookService import book_recommendations, books
import json


@app.route("/")
def index():
    return "Recommendation System"


@app.route("/book_recommendations", methods=['GET'])
def book_rec():
    input_book = request.args.get('book_liked')
    try:
        data = book_recommendations(input_book)

        return Response(data, mimetype='application/json')
    except Exception:
        return {"error": "Some error occured."}, 500

@app.route("/books", methods=['GET'])
def book_search():
    # input = request.args.get('q')
    try:
        data = books()

        return Response(data, mimetype='application/json')
    except Exception:
        return {"error": "Some error occured."}