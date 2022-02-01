from ast import literal_eval as to_dict
from config import CRYPT_KEY
import datetime
import jwt

class JwtCrypt:
    def encrypt(self, data: dict, time: int =5)-> str:
        try:
            return jwt.encode({
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=time),
                "data": str(data),
                "iat": datetime.datetime.utcnow()
            }, CRYPT_KEY, algorithm="HS256")
        except Exception as e:
            print(e)
            raise Exception("Error encrypt jwt")

    def decrypt(self, encoded_jwt: str)-> dict:
        try:
            return to_dict(jwt.decode(encoded_jwt, CRYPT_KEY, algorithms=["HS256"])['data'])
        except jwt.ExpiredSignatureError as e:
            raise Exception("JWT expired")
        except jwt.InvalidTokenError as e:
            raise Exception("Invalid JWT")
        except Exception as e:
            print(e)
            raise Exception("Error decrypt jwt")