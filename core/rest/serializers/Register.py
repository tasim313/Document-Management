from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from ...models import User
from ...choice import UserRole, UserStatus

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(
            required=True,
            label="Email",
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    role = serializers.ChoiceField(
           label="User Role",
           choices = UserRole.choices
    )

    password = serializers.CharField(write_only=True,
                                     required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'role', 'password', 'password2')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            role=validated_data['role'],
            user_status = UserStatus.Active,
            is_active = True,
            is_staff = True,
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user