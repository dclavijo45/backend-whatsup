from services.verify_number import VerifyNumberService
from validators.config.validator import Validator
from flask.views import MethodView
from flask import jsonify, request

class VerifyNumberController(MethodView):
    def post(self):
        try:
            if data := request.get_json():
                number = data['number'].strip() if data['number'] else ''
                device_id = data['device_id'].strip() if data['device_id'] else ''

                #Validate
                if Validator().size(number, 5, 15) or Validator().contain(number, '+'):
                    return jsonify({'message': "Invalid 'number'"}), 400

                if Validator().size(device_id, 5, 15):
                    return jsonify({'message': "Invalid 'device_id'"}), 400
                
                token = VerifyNumberService(number, device_id, request.remote_addr).getToken()

                return jsonify({'token': token}), 200

            return jsonify({'message': "Missing data"}), 400
        except KeyError as e:
            return jsonify({"message": f"Missing {str(e)}"}), 400
        except Exception as e:
            print(e)
            return jsonify({"message": "Internal server error"}), 500