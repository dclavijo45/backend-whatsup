from validators.user import UserValidator
from services.auth import AuthService
from flask.views import MethodView
from flask import jsonify, request

class RegisterController(MethodView):
    def post(self):
        try:
            if data := request.get_json():
                user_info = {
                    "name": data['name'].strip() if data['name'] else '',
                    "number": data['number'].strip() if data['number'] else '',
                    "device_id": data['device_id'].strip() if data['device_id'] else '',
                    "birthday": data['birthday'].strip() if data['birthday'] else '',
                    "username": data['username'].strip() if data['username'] else '',
                    "profile_image": None,
                    "description": data['description'].strip() if data['description'] else None,
                    "role": '1',
                    "status": '1'
                }

                #Validate
                if is_valid := UserValidator(user_info).validate():
                    return jsonify(is_valid), 400

                register = AuthService().register(user_info)

                if not register['registered']:
                    return jsonify(register), 401
                
                return jsonify(register), 200

            return jsonify({'message': "Missing data"}), 400
        except KeyError as e:
            return jsonify({"message": f"Missing {str(e)}"}), 400
        except Exception as e:
            print(e)
            return jsonify({"message": "Internal server error"}), 500
