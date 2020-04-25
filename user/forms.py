# users/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', ]
    #
    # def __init__(self):
    #     super(SignupForm, self).__init__()
    #     self.fields['username'].placeholder = 'Username'
