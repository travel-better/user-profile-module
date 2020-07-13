from flask import jsonify, request, g
from app import UserProfile
from http import HTTPStatus
from . import main
from datetime import datetime

@main.route('/userprofile', methods=['GET', 'POST'])
def profiles():
    if request.method == 'GET':
        profiles = UserProfile.all()
        response_data = []
        try:
            for profile in profiles.rows:
                response_data.append(profile.__dict__)
            return jsonify(response_data), HTTPStatus.OK
        except Exception as e:
            return jsonify({
                'message': 'Ensure `all` view is correctly defined in the `userprofile` design document',
                'error': e.args
              }), HTTPStatus.BAD_REQUEST

    if request.method == 'POST':
        profile = UserProfile(**request.get_json())
        profile.store()
        return jsonify({
            'message': 'Successfully added',
            'id': profile.id
            }), HTTPStatus.CREATED

    return HTTPStatus.BAD_REQUEST

@main.route('/userprofile/<string:profile_id>', methods=['GET', 'PUT', 'DELETE'])
def profile(profile_id):
    profile = UserProfile.load(id=profile_id)
    if not profile:
        return jsonify({
            'error': 'Profile not found.'
        }), HTTPStatus.BAD_REQUEST
    
    if request.method == 'GET':
        return jsonify(profile.__dict__), HTTPStatus.OK

    if request.method == 'PUT':
        profile = UserProfile(**request.get_json())
        profile.store()
        return jsonify({
            'message': 'Successfully Updated profile'
        }), HTTPStatus.OK

    if request.method == 'DELETE':
        g.couch.delete(profile)
        return jsonify({
            'message': 'Successfully deleted profile'
        }), HTTPStatus.OK

    return HTTPStatus.BAD_REQUEST