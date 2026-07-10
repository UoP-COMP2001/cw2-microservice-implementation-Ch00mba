from datetime import datetime

import pytz

from config import db, ma

#Table model - matches database table
class Subscription(db.Model):
    __tablename__ = "Subscription"
    __table_args__ = {"schema": "RCW2"}
    SubscriptionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, nullable=False)
    TierID = db.Column(db.Integer, nullable=False)
    SubscriptionStart = db.Column(db.Date, nullable=False)
    SubscriptionEnd = db.Column(db.Date, nullable=True)

class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription
        load_instance = True
        sql_session = db.session

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)