from dotenv import load_dotenv, find_dotenv
from os import getenv as env
from os import urandom
import random
import string

#App
load_dotenv(find_dotenv())
SECRET_KEY = ''.join(random.
    choice(f"{string.ascii_uppercase}{string.punctuation}{string.ascii_letters}") 
    for i in range(20))

DEBUG = int(env('DEBUG', '1'))

#Server
PORT = int(env('PORT', 5000))
HOST = env('HOST', 'localhost')

#MySQL
MYSQL_HOST = env('MYSQL_HOST', 'localhost')
MYSQL_USER = env('MYSQL_USER', 'root')
MYSQL_PASSWORD = env('MYSQL_PASSWORD', '')
MYSQL_DB = env('MYSQL_DB', None)

#Security
CRYPT_KEY = env('CRYPT_KEY', ''.join(random.
    choice(f"{string.ascii_uppercase}{string.punctuation}{string.ascii_letters}") 
    for i in range(20)))
CRYPT_SALT = urandom(16)

# APi SMS
SMS_URL_API = env('SMS_URL_API', None)
SMS_TOKEN_API = env('SMS_TOKEN_API', None)
SMS_URL_QUERY_API= env('SMS_URL_QUERY_API', None)