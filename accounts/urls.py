from django.urls import path
from .views import AdminCreateUserView, LoginView, UserProfileView, UserRoleView
urlpatterns = [
    path('admin/create-user/', AdminCreateUserView.as_view()),
    path('roles/', UserRoleView.as_view(), name='user-roles'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]