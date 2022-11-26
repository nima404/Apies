from django.urls import path
from .routers import router
from .views import UserRetrieveUpdateView, ChangePasswordView, PreRegisterView, RegisterView
from rest_framework.authtoken import views

app_name = 'user'

urlpatterns = [
    path('profile/', UserRetrieveUpdateView.as_view()),
    path('profile/change-password/', ChangePasswordView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('pre-register/', PreRegisterView.as_view()),
    path('register/', RegisterView.as_view())
] + router.urls
