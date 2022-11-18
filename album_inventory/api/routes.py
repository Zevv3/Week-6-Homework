from flask import Blueprint, request, jsonify
from album_inventory.helpers import token_required
from album_inventory.models import db, Album, album_schema, albums_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata', methods = ['GET'])
@token_required
def getdata(current_user_token):
    return { 'some': 'value'}

# Create
@api.route('/albums', methods = ['POST'])
@token_required
def create_album(current_user_token):
    album_title = request.json['album_title']
    artist_name = request.json['artist_name']
    year = request.json['year']
    genre = request.json['genre']
    number_of_tracks = request.json['number_of_tracks']
    label = request.json['label']
    user_token = current_user_token.token

    print(f"User Token: {current_user_token.token}")

    album = Album(album_title, artist_name, year, genre, number_of_tracks, label, user_token=user_token)

    db.session.add(album)
    db.session.commit()
    response = album_schema.dump(album)
    return jsonify(response)

# Get all
@api.route('/albums', methods = ['GET'])
@token_required
def get_albums(current_user_token):
    owner = current_user_token.token
    albums = Album.query.filter_by(user_token=owner).all()
    response = albums_schema.dump(albums)
    return jsonify(response)

# Get One
@api.route('drones/<id>', methods = ['GET'])
@token_required
def get_album(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        album = Album.query.get(id)
        response = album_schema.dump(album)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401

# Update
@api.route('/albums/<id>', methods = ['POST', 'PUT'])
@token_required
def update_album(current_user_token, id):
    album = Album.query.get(id)
    album.album_title = request.json['album_title']
    album.artist_name = request.json['artist_name']
    album.year = request.json['year']
    album.genre = request.json['genre']
    album.number_of_tracks = request.json['number_of_tracks']
    album.label = request.json['label']
    album.user_token = current_user_token.token
    db.session.commit()
    response = album_schema.dump(album)
    return jsonify(response)

# Delete
@api.route('/albums/<id>', methods = ['DELETE'])
@token_required
def delete_album(current_user_token, id):
    album = Album.query.get(id)
    db.session.delete(album)
    db.session.commit()
    response = album_schema.dump(album)
    return jsonify(response)