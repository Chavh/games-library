
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import uuid
import data as da
import common as cn

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})

@app.route('/games', methods=['GET'])
def all_games():
    games = da.fetch_games()
    if games:
        response_object = {'status': 'success', 'games': games}
        return make_response(jsonify(response_object)), 200
    else:
        response_object = {'status': 'fail', 'message': 'Error while fetching games!'}
        return make_response(jsonify(response_object)), 500


@app.route('/games', methods=['POST'])
def add_game():
    # Get the request data
    request_data = request.get_json()
    title = request_data.get('title')
    genre = request_data.get('genre')
    played = request_data.get('played')
    id =  str(cn.concat_and_hash(title,genre))
    # Add the game
    success = da.add_game(id, title, genre, played)

    # Return the response
    if success:
        response_object = {'status': 'success', 'message': 'Game added!'}
        return make_response(jsonify(response_object)), 200
    else:
        response_object = {'status': 'success', 'message': 'Error while adding game!'}
        return make_response(jsonify(response_object)), 500

@app.route('/games/<game_id>', methods=['PUT'])
def update_game(game_id):
    # Get the request data
    request_data = request.get_json()
    title = request_data.get('title')
    genre = request_data.get('genre')
    played = request_data.get('played')

    # Update the game
    success = da.update_game(game_id, title, genre, played)

    # Return the response
    if success:
        response_object = {'status': 'success', 'message': 'Game updated!'}
        return make_response(jsonify(response_object)), 200
    else:
        response_object = {'status': 'success', 'message': 'Error while updating game!'}
        return make_response(jsonify(response_object)), 500

@app.route('/games/<game_id>', methods=['DELETE'])
def delete_game(game_id):
    # Delete the game
    success = da.delete_game(game_id)

    # Return the response
    if success:
        response_object = {'status': 'success', 'message': 'Game deleted!'}
        return make_response(jsonify(response_object)), 200
    else:
        response_object = {'status': 'success', 'message': 'Error while deleting game!'}
        return make_response(jsonify(response_object)), 500