from utils.ma import ma

class LoginAttemptsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'number', 'ip_address', 'attempts', 'device_id', 'created_at', 'updated_at')

login_attempt = LoginAttemptsSchema()

login_attempts = LoginAttemptsSchema(many=True)