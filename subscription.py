from flask import abort, make_response

from config import db
from models import Subscription, subscription_schema, subscriptions_schema

#CRUD OPERATIONS

#Read all
def read_all():
    subscriptions = Subscription.query.all()
    return subscriptions_schema.dump(subscriptions)

#Read one
def read_one(SubscriptionID):
    subscription = Subscription.query.filter(Subscription.SubscriptionID == SubscriptionID).one_or_none()

    if subscription is not None:
        return subscription_schema.dump(subscription)
    else:
        abort(404, f"subscription with id {SubscriptionID} not found")

#Create
def create(subscription):
    new_sub = subscription_schema.load(subscription, session=db.session)
    db.session.add(new_sub)
    db.session.commit()
    return subscription_schema.dump(new_sub), 201

#Update
def update(SubscriptionID, subscription):
    existing_sub = Subscription.query.filter(Subscription.SubscriptionID == SubscriptionID).one_or_none()

    if existing_sub:
        update_subscription = subscription_schema.load(subscription, session=db.session)
        existing_sub.UserID = update_subscription.UserID
        existing_sub.TierID = update_subscription.TierID
        existing_sub.SubscriptionStart = update_subscription.SubscriptionStart
        existing_sub.SubscriptionEnd = update_subscription.SubscriptionEnd

        db.session.merge(existing_sub)
        db.session.commit()

        return subscription_schema.dump(existing_sub), 200
    else:
        abort(404, f"Subscription with ID {SubscriptionID} not found")

#Delete
def delete(SubscriptionID):
    existing_sub = Subscription.query.filter(Subscription.SubscriptionID == SubscriptionID).one_or_none()

    if existing_sub:
        db.session.delete(existing_sub)
        db.session.commit()
        return make_response(f"{SubscriptionID} successfully deleted", 200)
    else:
        abort(404, f"Subscription with id {SubscriptionID} not found")