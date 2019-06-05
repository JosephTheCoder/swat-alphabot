import sqlalchemy
from app.models.users import Users

class UserFinder(object):

    @classmethod
    def get_from_username(cls, username):
        return Users.query.filter_by(username=username).first()