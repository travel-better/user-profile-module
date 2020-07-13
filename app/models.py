from flaskext.couchdb import (
    Document, Mapping, TextField, IntegerField, BooleanField, DateTimeField, FloatField, DictField, ListField, ViewField
)
from datetime import datetime

class UserProfile(Document):
    '''
    Document for the user profile database
    '''

    doc_type = 'userprofile'

    first_name = TextField()
    last_name = TextField()
    address = TextField()
    email = TextField()
    bio = TextField()
    total_reward_points = FloatField(default=0.0)
    current_redeemable_points = FloatField(default=0.0)
    user_total_carbon_footprint = FloatField(default=0.0)
    total_possible_carbon_footprint = FloatField(default=0.0)
    total_carbon_footprint_reduced = FloatField(default=0.0)
    total_user_activities = IntegerField(default=0)
    created_at = DateTimeField(default=datetime.now())
    activities = ListField(DictField(Mapping.build(
        activity_name = TextField(),        
        activity_type = TextField(),
        activity_start_date = DateTimeField()
        activity_end_date = DateTimeField()
        activity_total_possible_carbon = FloatField(default=0.0),
        activity_carbon_reduced = FloatField(default=0.0),
        activity_reward_points = FloatField(default=0.0)
        isRewardRedeemed = BooleanField(default=False),
    )))
    points = ListField(DictField(Mapping.build(
        total_points = FloatField(default=0.0),
        redeem_date = DateTimeField(),
        redeem_item = TextField()
    )))
    
    all = ViewField('userprofile', '''
    function (doc) {
        if (doc.doc_type == 'userprofile') {
            emit(doc.username, doc);
        };
    }''')