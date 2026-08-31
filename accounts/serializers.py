from rest_framework import serializers
from .models import User, Role
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField() # instead of getting role id, youll get role name
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'first_name', 'last_name']
        read_only_fields = fields

class UserRole(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)
#     password = serializers.CharField(write_only=True)
    
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'role', 'first_name', 'last_name', 'confirm_password', 'password']
        

#     def validate(self, attrs):
#         password = attrs.get('password')
#         confirm_password = attrs.get('confirm_password')

#         if password != confirm_password:
#             raise serializers.ValidationError("Passwords do not match.")

#         return attrs

#     def create(self, validated_data):
#         validated_data.pop("confirm_password")
#         return User.objects.create_user(**validated_data)


class AdminCreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'password']

    def validate_role(self, role):
        if role.name.lower() == 'admin':
            raise serializers.ValidationError(
                "Admin accounts can only be created via createsuperuser."
            )
        return role

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        data['user'] = user
        return data

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
        ]