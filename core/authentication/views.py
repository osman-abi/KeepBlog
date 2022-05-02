from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from .forms import LoginForm, RegisterForm
# Create your views here.
from .models import User


class RegisterUser(FormView):
    template_name = 'registration/register.html'
    success_url = '/success/'
    form_class = RegisterForm

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        return super(RegisterUser, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'registration/login.html'
    success_url = '/success/'
    form_class = LoginForm
    
    def form_valid(self, form):
        user = form.get_user()
        login(request=self.request, user=user)
        return super(LoginUser, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(LoginUser, self).form_invalid(form)



