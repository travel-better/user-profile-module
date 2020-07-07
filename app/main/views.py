from flask import jsonify, request
from app import UserProfile
from http import HTTPStatus
from . import main

@main.route('/userprofile', methods=['GET', 'POST'])
def get_profiles():

    if request.method == 'GET':
        profiles = UserProfile.all()
        response_data = []
        for profile in profiles:
            data = {
                'id': profile.id,
                'username': profile.username,
                'bio': profile.bio,
                'total_reward_points': profile.total_reward_points,
                'current_redeemable_points': profile.current_redeemable_points,
                'user_total_carbon_footprint': profile.user_total_carbon_footprint,
                'total_possible_carbon_footprint': profile.total_possible_carbon_footprint,
                'total_carbon_footprint_reduced': profile.total_carbon_footprint_reduced,
                'total_user_activities': profile.total_user_activities,
            }
            response_data.append(data)
        return jsonify(response_data), HTTPStatus.OK

    if request.method == 'POST':
        request_data = request.get_json()
        profile_data = dict(
            username = request_data.get('username'),

        )
        profile = UserProfile(**profile_data)
        profile.store()
        return HTTPStatus.CREATED

    return HTTPStatus.BAD_REQUEST

@main.route('/userprofile/<int:profile_id>/', methods=['GET', 'PUT', 'DELETE'])
def single_profile(profile_id):
    profile = UserProfile.load(id=profile_id)
    if not profile:
        return jsonify({
            'error': 'Profile not found.'
        }), HTTPStatus.BAD_REQUEST
    
    if request.method == 'GET':
        response_data = {
            'id': profile.id,
            'username': profile.username,
            'bio': profile.bio,
            'total_reward_points': profile.total_reward_points,
            'current_redeemable_points': profile.current_redeemable_points,
            'user_total_carbon_footprint': profile.user_total_carbon_footprint,
            'total_possible_carbon_footprint': profile.total_possible_carbon_footprint,
            'total_carbon_footprint_reduced': profile.total_carbon_footprint_reduced,
            'total_user_activities': profile.total_user_activities,
        }

        return response_data, HTTPStatus.OK

    if request.method == 'PUT':
        request_data = request.get_json()
        profile_data = dict(
            username = request_data.get('username'),

        )
        profile = UserProfile(**profile_data)
        profile.store()
        return jsonify({
            'message': 'Successfully Updated profile'
        }), HTTPStatus.OK

    if request.method == 'DELETE':
        profile['_deleted'] = True
        return jsonify({
            'message': 'Successfully deleted profile'
        }), HTTPStatus.OK

    return HTTPStatus.BAD_REQUEST