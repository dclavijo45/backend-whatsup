from models.users import User
from schemas.user import user
from utils.db import db

class UserService:
    def getUserByNumber(self, number: str)-> dict:
        try:
            user_query = User.query.filter_by(number=number).first()
            return user.dump(user_query)
        except Exception as e:
            print(e)
            raise Exception('Get user by number failed')
    
    def createUser(self, user_info: dict)-> dict:
        try:
            new_user = User(user_info['name'], user_info['number'], user_info['birthday'], user_info['username'], user_info['profile_image'], user_info['description'], user_info['role'], user_info['status'])
            db.session.add(new_user)
            db.session.commit()
            return user.dump(new_user)
        except Exception as e:
            print(e)
            raise Exception('Create user failed')
