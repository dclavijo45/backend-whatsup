from services.login_attempt import LoginAttemptsService
from services.user import UserService
from utils.jwt_crypt import JwtCrypt
from utils.pwd_crypt import PwdCrypt

class AuthService:
    def login(self, number: str, device_id: str, token: str, ip_address: str, verification_code: str)-> dict:
        result = {'logged_in': False, 'message': 'User is not registered'}

        try:
            user_info = UserService().getUserByNumber(number)
            if len(user_info) > 0:
                check_token = self.__check_token(token, number, device_id, ip_address, verification_code)
                if not check_token['success']:
                    result['message'] = check_token['message']
                    return result

                result['user'] = {
                    'id': user_info['id'],
                    'name': user_info['name'],
                    'number': user_info['number'],
                    'birthday': user_info['birthday'],
                    'username': user_info['username'],
                    'profile_image': user_info['profile_image'],
                    'description': user_info['description'],
                    'role': user_info['role'],
                    'status': user_info['status'],
                    'device_id': device_id
                }
                result['logged_in'] = True
                result['message'] = 'Login successful'
                result['token'] = JwtCrypt().encrypt({
                    'number': number,
                    'role': user_info['role'],
                    'status': user_info['status'],
                    'device_id': device_id
                })
            
            return result
        except Exception as e:
            print(e)
            raise Exception('Login failed')

    def register(self, user_info: dict)-> dict:
        result = {'registered': False, 'message': 'User is already registered'}

        try:
            userService = UserService()
            if len(userService.getUserByNumber(user_info['number'])) > 0:
                return result
            
            userService.createUser(user_info)

            result['registered'] = True
            result['message'] = 'Register successful'
            
            return result
        except Exception as e:
            print(e)
            raise Exception('Register failed')

    def __check_token(self, token: str, number: str, device_id: str, ip_address: str, verification_code: str)-> dict:
        result = {'success': False, 'message': 'Invalid token'}

        try:
            decrypted_token = JwtCrypt().decrypt(token)

            if decrypted_token['number'] != number:
                return result
            if decrypted_token['ip_address'] != ip_address:
                return result
            if decrypted_token['device_id'] != device_id:
                return result
            if PwdCrypt().decrypt(decrypted_token['verification_code']) != verification_code:
                result['message'] = 'Invalid code'
                return result
            
            verify_attempt = LoginAttemptsService().verify_login_attempt(PwdCrypt().decrypt(decrypted_token['attempt_id']), number, device_id)

            if not verify_attempt['verified']:
                result['message'] = verify_attempt['message']
                return result

            result['success'] = True
            result['message'] = 'Valid token'
            return result

        except KeyError as e:
            print(f"Missing in token {str(e)}")
            return result
        except Exception as e:
            print(e)
            return result
