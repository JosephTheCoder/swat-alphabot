import sqlalchemy
from app.models.user import User

class UserFinder(object):

    @classmethod
    def get_from_username(cls, username):
        return User.query.filter_by(username=username).first()