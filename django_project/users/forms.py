from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


domain_choices = (
    ('Software Development', 'Software Development'),
    ('Web Development', 'Web Development'),
    ('Web Design', 'Web Design'),
    ('Cyber Security', 'Cyber Security'),
    ('Financial Technology', 'Financial Technology'),
)


abilities_choices = (
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('Java', 'Java'),
    ('C++', 'C++'),
    ('C#', 'C#'),
    ('Go', 'Go'),
    ('Ruby', 'Ruby'),
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('Swift', 'Swift'),
    ('SQL', 'SQL'),
)


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    description = forms.CharField()
    domain = forms.ChoiceField(choices=domain_choices)
    years_of_experience = forms.IntegerField()
    abilities_1 = forms.ChoiceField(choices=abilities_choices)
    abilities_2 = forms.ChoiceField(choices=abilities_choices)
    abilities_3 = forms.ChoiceField(choices=abilities_choices)
    abilities_4 = forms.ChoiceField(choices=abilities_choices)
    github_info = forms.URLField()
    linkedin_info = forms.URLField()

    class Meta:
        model = Profile
        fields = [
                'image', 'first_name', 'last_name',
                  'description', 'domain', 'years_of_experience', 
                  'abilities_1', 'abilities_2', 'abilities_3', 'abilities_4',
                  'github_info', 'linkedin_info'
                  ]
