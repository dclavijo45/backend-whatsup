from models.login_attempts import LoginAttempts
from schemas.login_attempt import login_attempt
from datetime import timedelta, datetime
from dateutil import parser as parseTime
from utils.db import db
class LoginAttemptsService:
    def create_login_attempt(self, number: str, ip_address: str, device_id: str)-> dict:
        try:
            login_attempt_data = {
                'number': number,
                'ip_address': ip_address,
                'attempts': 0,
                'device_id': device_id,
            }
            new_login_attempt = LoginAttempts(**login_attempt_data)
            db.session.add(new_login_attempt)
            db.session.commit()
            return login_attempt.dump(new_login_attempt)
        except Exception as e:
            print(e)
            raise Exception('Create login attempt failed')

    def verify_login_attempt(self, attempt_id: int, number: str, device_id: str)-> dict:
        result = {'verified': False, 'message': 'Invalid attempt'}

        try:
            login_attempt_query = LoginAttempts.query.filter_by(id=attempt_id).first()
            if len(login_attempt.dump(login_attempt_query)) > 0:
                attempt_data = login_attempt.dump(login_attempt_query)
                if parseTime.parse(attempt_data['updated_at']) + timedelta(minutes=5) > datetime.now():
                    attempt_data['attempts'] += 1
                    if attempt_data['attempts'] <= 4:
                        login_attempt_query.attempts = attempt_data['attempts']
                        db.session.commit()
                        if number != attempt_data['number'] or device_id != attempt_data['device_id']:
                            result['message'] = 'Invalid token'
                            return result

                        result['verified'] = True
                        result['message'] = 'Login attempt verified'
                        return result
                    else:
                        result['message'] = 'Maximum attempts reached'
                        return result
                else:
                    result['message'] = 'Invalid token'
                    return result

            return result
        except KeyError as e:
            print(f"Missing in data {str(e)}")
            raise Exception('Verify login attempt failed')
        except Exception as e:
            print(e)
            raise Exception('Verify login attempt failed')

    def get_login_attempt(self, attempt_id: int)-> dict:
        try:
            login_attempt_query = LoginAttempts.query.filter_by(id=attempt_id).first()
            if len(login_attempt.dump(login_attempt_query)) > 0:
                return login_attempt.dump(login_attempt_query)
            raise Exception('Login attempt not found')
        except Exception as e:
            print(e)
            raise Exception('Get login attempt failed')
