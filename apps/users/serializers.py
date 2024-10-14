from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
