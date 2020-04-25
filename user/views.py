from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import SignupForm
from user.models import Client


class SignupView(CreateView):
    model = Client
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('blog:home')