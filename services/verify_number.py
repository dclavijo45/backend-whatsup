from config import SMS_TOKEN_API, SMS_URL_API, SMS_URL_QUERY_API
from services.login_attempt import LoginAttemptsService
from utils.pwd_crypt import PwdCrypt
from utils.jwt_crypt import JwtCrypt
from requests import get
import random
import string

class VerifyNumberService:
    def __init__(self, number: str, device_id: str, ip_address: str):
        self.__ip_address = ip_address
        self.__device_id = device_id
        self.__verification_code = ''
        self.__number = number
        self.__attempt_id = -1
        self.__token = ''

        if not self.__generate_verification_code():
            raise Exception('Verification code has not been generated')

        if not self.__generate_login_attempt():
            raise Exception(f"Login attempt has not been generated for number: {self.__number}")

        if not self.__send_sms_verification_code():
            raise Exception(f"SMS verification code has not been sent for number: {self.__number}")

        if not self.__generate_token():
            raise Exception(f"Token has not been generated for number: {self.__number}")
    
    def __generate_verification_code(self)-> bool:
        try:
            self.__verification_code = ''.join(random.choice(string.digits) for _ in range(6))
            return True
        except Exception as e:
            print(e)
            return False

    def __send_sms_verification_code(self)-> bool:
        try:
            current_balance = get(f"{SMS_URL_QUERY_API}{SMS_TOKEN_API}").text
            if float(current_balance) > 1:
                message = f"WhatsUp code: {self.__verification_code}"
                send_sms = get(f"{SMS_URL_API}{SMS_TOKEN_API}&message={message}&numero={self.__number[1::]}").text
                if 'Accepté' in send_sms:
                    return True

                print(f"SMS has not been sent, response: {send_sms}")
                return False

            print(f"Not enough balance for send SMS, current balance: {current_balance}")
            return False
        except Exception as e:
            print(e)
            return False
    
    def __generate_login_attempt(self)-> bool:
        try:
            login_attempt = LoginAttemptsService().create_login_attempt(self.__number, self.__ip_address, self.__device_id)
            self.__attempt_id = login_attempt['id']
            return True
        except Exception as e:
            print(e)
            return False

    def __generate_token(self)->bool:
        try:
            if self.__attempt_id == -1 or self.__verification_code == '':
                return False
            
            self.__token = JwtCrypt().encrypt({
                'number': self.__number,
                'verification_code': PwdCrypt().encrypt(self.__verification_code),
                'device_id': self.__device_id,
                'ip_address': self.__ip_address,
                'attempt_id': PwdCrypt().encrypt(str(self.__attempt_id)),
            })
            return True
        except Exception as e:
            print(e)
            return False

    def getToken(self)-> str:
        if self.__token == '':
            raise Exception('Token has not been generated')
        return self.__token