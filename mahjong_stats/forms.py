from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Stats
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus.widgets import DatePickerInput

User = get_user_model()
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("username",  "password1", "password2")

class DataAddForm(forms.ModelForm):
    class Meta:
        model=Stats
        fields="__all__"
        widgets = {
            'date': DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MM月 DD日',
                }
            ),
            'user':forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    def clean(self):
        data = super().clean()
        counts = data["counts"]
        first  = data["first"]
        second = data["second"]
        third  = data["third"]
        fourth = data["fourth"]
        if counts!=first+second+third+fourth:
            raise ValidationError("打荘回数が間違っています。")
        return data


