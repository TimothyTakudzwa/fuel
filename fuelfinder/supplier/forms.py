from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import SupplierProfile, FuelUpdate, FuelRequest, Province


class PasswordChange(PasswordChangeForm):
    class Meta:
        widgets = {

        }
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class RegistrationForm(UserCreationForm):
    class Meta:
        widgets = {
            'password': forms.PasswordInput()
        }

        model = User
        fields = ['username', 'password1', 'password2']


class RegistrationProfileForm(forms.ModelForm):
    class Meta:
        model = SupplierProfile
        fields = ['bpn', 'phone', 'street', 'city', 'province']


class RegistrationEmailForm(forms.Form):
    email = forms.EmailField()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = SupplierProfile
        fields = ['bpn', 'phone', 'street', 'city', 'province']


class ProfilePictureUpdateForm(forms.ModelForm):
    class Meta:
        model = SupplierProfile
        fields = ['picture']


class FuelRequestForm(forms.ModelForm):
    class Meta:
        model = FuelRequest
        fields = ['amount', 'split', 'payment_method', 'delivery_method', 'location', 'fuel_type']
