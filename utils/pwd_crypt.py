from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from config import CRYPT_KEY, CRYPT_SALT
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode

class PwdCrypt:
    def encrypt(self, value: str)->str:
        try:
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=CRYPT_SALT, iterations=100)
            key = urlsafe_b64encode(kdf.derive(CRYPT_KEY.encode('utf-8')))
            return Fernet(key).encrypt(value.encode('utf-8')).decode('utf-8')
        except Exception as e:
            print(e)
            raise Exception('Encrypt crypt with pwd failed')

    def decrypt(self, value: str)->str:
        try:
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=CRYPT_SALT, iterations=100)
            key = urlsafe_b64encode(kdf.derive(CRYPT_KEY.encode('utf-8')))
            return Fernet(key).decrypt(value.encode('utf-8')).decode('utf-8')
        except Exception as e:
            print(e)
            raise Exception('Decrypt crypt with pwd failed')

