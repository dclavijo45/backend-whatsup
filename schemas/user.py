from utils.ma import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'number', 'birthday', 'username', 'profile_image', 'role', 
                        'description', 'status', 'created_at', 'updated_at')

user = UserSchema()

users = UserSchema(many=True)