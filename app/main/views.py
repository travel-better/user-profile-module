from flask import jsonify, request
from app import UserProfile
from http import HTTPStatus
from . import main

@main.route('/userprofile', methods=['GET'])
def get_profiles():
    profiles = UserProfile.all()
    response_data = []
    for profile in profiles:
        data = {
            'id': profile.id,
            'username': profile.username,

        }
        response_data.append(data)
    return jsonify(response_data), HTTPStatus.OK

@main.route('/userprofile', methods=['POST'])
def create_profile():
    request_data = request.get_json()
    profile_data = dict(
        username = request_data.get('username'),

    )
    profile = UserProfile(**profile_data)
    profile.store()
    return HTTPStatus.CREATED

@main.route('/userprofile/<string:profile_id>/', methods=['GET'])
def retrieve_profile(profile_id):
    profile = UserProfile.load(id=profile_id)
    if not profile:
        return jsonify({
            'error': 'Profile not found.'
        }), HTTPStatus.BAD_REQUEST
    
    response_data = {
        'id': profile.id,
        'username': profile.username,

    }

    return response_data, HTTPStatus.OK