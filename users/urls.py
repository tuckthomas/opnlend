from django.urls import path, include
from registration.backends.default.views import RegistrationView
from .views import ProfileView
from .views import UserLoginView, UserLogoutView, UserRegistrationView, ProfileView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('accounts/register/', RegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.default.urls')),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

