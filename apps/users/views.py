from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser

from core.permissions.custom_permissions import IsAdminOrWriteOnly

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class UserListCreateAPIView(ListCreateAPIView):
    """
    get:
        List of users
    post:
        Create a new user
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)


class UserRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """
    get:
        return user by id
    delete:
        delete user by id
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)
