from flaskext.couchdb import Document, Mapping, TextField, IntegerField, BooleanField, DateTimeField, FloatField, DictField, ListField
from datetime import datetime

class UserProfile(Document):
    '''
    Document for the user profile database
    '''

    doc_type = 'userprofile'

    username = TextField()
    bio = TextField()
    total_reward_points = FloatField(default=0.0)
    current_redeemable_points = FloatField(default=0.0)
    user_total_carbon_footprint = FloatField(default=0.0)
    total_possible_carbon_footprint = FloatField(default=0.0)
    total_carbon_footprint_reduced = FloatField(default=0.0)
    total_user_activities = IntegerField(default=0)
    created_at = DateTimeField(default=datetime.now())
    activities = ListField(DictField(Mapping.build(
        activity_name = TextField()
        activity_destination = FloatField(default=0.0)
        activity_completed = BooleanField(default=False)
        activity_route_taken = TextField()
        activity_time_taken = IntegerField(default=0) #Time in minutes
        activity_total_possible_carbon = FloatField(default=0.0)
        activity_carbon_used = FloatField(default=0.0)
        activity_reward_points = FloatField(default=0.0)
    )))
    points = ListField(DictField(Mapping.build(
        points = FloatField(default=0.0)
        redeem_date = DateTimeField()
        redeem_item = TextField()
    )))