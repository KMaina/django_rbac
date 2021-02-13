from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    """The serialzier to serialize customer creation"""
    password = serializers.CharField(min_length=4, max_length=100)
    username = serializers.CharField(max_length=100,
                                     required=True,
                                     validators=[
                                        UniqueValidator(
                                            queryset=User.objects.all())
                                        ])
    email = serializers.CharField(max_length=100,
                                  required=True,
                                  validators=[
                                        UniqueValidator(
                                            queryset=User.objects.all())
                                            ])

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class AttendantRegistrationSerializer(serializers.ModelSerializer):
    """The serialzier to serialize attendant creation"""
    password = serializers.CharField(min_length=4, max_length=100)
    username = serializers.CharField(max_length=100,
                                     required=True,
                                     validators=[
                                        UniqueValidator(
                                            queryset=User.objects.all())])
    email = serializers.CharField(max_length=100,
                                  required=True,
                                  validators=[
                                        UniqueValidator(
                                            queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self, validated_data):
        user = User.objects.create_attendant(**validated_data)
        return user
