from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


dataframe = pd.read_csv('./imdb-movie-data.csv')


def filter_by_genre(genre):
    return dataframe[dataframe['Genre'].str.contains(genre, case=False, na=False)].to_dict(orient='records')

@app.route('/', methods=['GET'])
def get_movies_by_genre():
    genre = request.args.get('genre')
    if not genre:
        return jsonify({"error": "Please provide a genre parameter"}), 400
    movies = filter_by_genre(genre)
    return jsonify(movies)

@app.route('/action', methods=['GET'])
def get_action_movies():
    return jsonify(filter_by_genre('Action'))

@app.route('/adventure', methods=['GET'])
def get_adventure_movies():
    return jsonify(filter_by_genre('Adventure'))

@app.route('/comedy', methods=['GET'])
def get_comedy_movies():
    return jsonify(filter_by_genre('Comedy'))

@app.route('/drama', methods=['GET'])
def get_drama_movies():
    return jsonify(filter_by_genre('Drama'))

@app.route('/romance', methods=['GET'])
def get_romance_movies():
    return jsonify(filter_by_genre('Romance'))

@app.route('/western', methods=['GET'])
def get_western_movies():
    return jsonify(filter_by_genre('Western'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
