from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if "password" in validated_data:
                instance.set_password(validated_data["password"])
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model= User
        fields= [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
            "password": {"write_only": True},
            "first_name": {"max_length": 50},
            "last_name": {"max_length": 50},
            "is_superuser": {"read_only": True},
        }