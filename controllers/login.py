from validators.config.validator import Validator
from services.auth import AuthService
from flask.views import MethodView
from flask import jsonify, request

class LoginController(MethodView):
    def post(self):
        try:
            #Verify number and code
            if token := request.headers.get("Authorization").split(" ")[1] if request.headers.get("Authorization") else None:
                pass
            else:
                return jsonify({"message": "Missing 'token'"}), 400
            
            if data := request.get_json():
                number = data['number'].strip() if data['number'] else ''
                device_id = data['device_id'].strip() if data['device_id'] else ''
                verification_code = data['verification_code'] if data['verification_code'] else ''

                #Validate
                validator = Validator()
                if validator.size(number, 5, 15) or validator.contain(number, '+') or validator.only_numbers(number[1::]):
                    return jsonify({'message': "Invalid 'number'"}), 400

                if validator.size(device_id, 5, 15):
                    return jsonify({'message': "Invalid 'device_id'"}), 400

                if validator.size(verification_code, 6, 6) or validator.only_numbers(verification_code):
                    return jsonify({'message': "Invalid 'verification_code'"}), 400

                response = AuthService().login(number, device_id, token, request.remote_addr, verification_code)

                if not response['logged_in']:
                    return jsonify(response), 401
                
                return jsonify(response), 200
            
            return jsonify({'message': "Missing data"}), 400
        except KeyError as e:
            return jsonify({"message": f"Missing {str(e)}"}), 400
        except Exception as e:
            print(e)
            return jsonify({"message": "Internal server error"}), 500
