from django.urls import path
from . import views

urlpatterns = [
               path('register/', views.UserRegistrationView.as_view(), name='user_registration'),
               path('login/', views.UserLoginView.as_view(), name='user_login'),
               path('<int:pk>/profile/', views.UserProfile.as_view(), name='user_profile')
]
