from django.urls import path

from apps.users.views import UserListCreateAPIView, UserRetrieveDestroyAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserRetrieveDestroyAPIView.as_view(), name='user_retrieve_destroy'),
]
