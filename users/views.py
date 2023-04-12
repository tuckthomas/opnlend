from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomRegistrationForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

class UserLogoutView(LogoutView):
    next_page = '/'

class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('profile')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
