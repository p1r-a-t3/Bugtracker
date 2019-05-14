from rest_framework import serializers

from bugtracker.model_managers.models import *


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectToken
        fields = ('project', 'token', 'refresh_token', 'time_to_live')


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errors
        fields = ('error_name', 'error_description', 'point_of_origin', 'reference_project')


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = "__all__"

    def create(self, validated_data):
        validated_data['_id'] = uuid4()
        validated_data['token'] = uuid4()
        validated_data['refresh_token'] = uuid4()
        validated_data['generated_at'] = timezone.now()
        return UserToken(**validated_data)


class UserRegistrationSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('user_email', 'user_name', 'password', 'is_admin')

    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        validated_data['user_id'] = uuid4()
        validated_data['updated_at'] = timezone.now()
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    @staticmethod
    def validate_email(value):
        # if not email_is_valid(value):
        #     raise serializers.ValidationError('Please use a different email address provider.')

        if User.objects.filter(user_email=value).exists():
            raise serializers.ValidationError('Email already in use, please use a different email address.')
        return value