from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'age', 'directon', 'balance', 'wallet_address')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255, write_only = True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only = True
    )

    class Meta:
        model = User
        fields = ('username', 'phone', 'age', 'directon', 'password', 'password2', 'balance', 'wallet_address')

def validate(self, attrs):
    if attrs['password'] != attrs['passwords2']:
        raise serializers.ValidationError ({'password2': 'Пароли отличаются'})
    if '+996' not in attrs['phone']:
        raise serializers.ValidationError({'phone': 'Введенный номер не соответствует стандартам КР (+996)'})
    return attrs

def create(self, validate_data):
    user = User.objects.create(
        username = validate_data['username'],
        phone = validate_data['phone'],
        age = validate_data['age'],
        direction = validate_data['direction'],
        password = validate_data['password']
    )
    user.set_password(validate_data['password'])
    user.save()
    return user
    

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone', 'age', 'directon', 'password', 'password2', 'balance', 'wallet_address')

